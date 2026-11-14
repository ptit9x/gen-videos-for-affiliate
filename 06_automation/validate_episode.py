#!/usr/bin/env python3
"""Kiểm tra hồ sơ offline; không gửi job Flow và không chứng nhận QC media."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import re
import sys

try:
    import yaml
    from jsonschema import Draft202012Validator
except ImportError:
    sys.exit('Requires jsonschema and PyYAML; see 06_automation/README.md')


def validate(episode, stage=None):
    episode = Path(episode).resolve()
    errors = []
    schema = json.loads((Path(__file__).parent / 'schemas/episode.schema.json').read_text())
    data = yaml.safe_load((episode / 'episode.yaml').read_text())
    for error in Draft202012Validator(schema).iter_errors(data):
        errors.append(f"{'/'.join(map(str, error.absolute_path)) or 'root'}: {error.message}")
    if errors:
        return errors

    def local_file(relative):
        parts = PurePosixPath(relative)
        if parts.is_absolute() or '..' in parts.parts or '\\' in relative or ':' in relative:
            errors.append(f'unsafe path: {relative}')
            return None
        target = (episode / relative).resolve()
        if not target.is_relative_to(episode) or not target.is_file():
            errors.append(f'missing or escaped asset: {relative}')
            return None
        return target

    def asset(value, prompt=False):
        if value is None:
            return
        target = local_file(value['path'])
        if target is None:
            return
        raw = target.read_bytes()
        if not raw:
            errors.append(f"empty asset: {value['path']}")
        if hashlib.sha256(raw).hexdigest() != value['sha256']:
            errors.append(f"checksum mismatch: {value['path']}")
        if prompt:
            try:
                text = raw.decode('utf-8').strip()
            except UnicodeDecodeError:
                errors.append(f"prompt must be UTF-8: {value['path']}")
                return
            if not text or re.search(r'\[[^\]]+\]|\{\{|\b(?:TODO|TBD|DRAFT)\b', text, re.I):
                errors.append(f"empty or unresolved prompt: {value['path']}")

    ids = [shot['shot_id'] for shot in data['shots']]
    if len(set(ids)) != len(ids):
        errors.append('duplicate shot_id')
    takes = {}
    for shot in data['shots']:
        sid = shot['shot_id']
        for field in ('image_prompt', 'motion_prompt'):
            asset(shot[field], prompt=True)
        asset(shot['first_frame'])
        for source in shot['image_sources']:
            asset(source)
        if shot['frame_status'] == 'approved' and shot['first_frame'] is None:
            errors.append(f'{sid}: approved frame missing')
        for take in shot['takes']:
            key = (sid, take['take_id'])
            if key in takes:
                errors.append(f'{sid}: duplicate take_id')
            takes[key] = take
            asset(take['file'])
        if stage == 'generation':
            if not shot['approved_for_generation']:
                errors.append(f'{sid}: not approved for generation')
            if shot['first_frame'] is None or shot['frame_status'] != 'approved':
                errors.append(f'{sid}: approved local first frame required')
            if not shot['image_sources']:
                errors.append(f'{sid}: image editing sources required')
            if shot['image_prompt'] is None or shot['motion_prompt'] is None:
                errors.append(f'{sid}: separate image and motion prompts required')
            elif shot['image_prompt']['path'] == shot['motion_prompt']['path']:
                errors.append(f'{sid}: image and motion prompts must be separate')
            if shot['first_frame'] is not None and any(
                shot['first_frame']['sha256'] == source['sha256']
                or shot['first_frame']['path'] == source['path']
                for source in shot['image_sources']
            ):
                errors.append(f'{sid}: identity source cannot substitute for a scene frame')

    manifest = yaml.safe_load((episode / 'edit/manifest.yaml').read_text())
    if not isinstance(manifest, dict):
        return errors + ['manifest must be an object']
    for field in ('schema_version', 'episode_id', 'revision'):
        if manifest.get(field) != data[field]:
            errors.append(f'manifest {field} differs from episode')
    selected = manifest.get('selected_takes')
    if not isinstance(selected, list):
        return errors + ['manifest selected_takes must be an array']
    selected_ids = []
    for selection in selected:
        if not isinstance(selection, dict):
            errors.append('manifest selection must be an object')
            continue
        sid = selection.get('shot_id')
        tid = selection.get('take_id')
        if not isinstance(sid, str) or not isinstance(tid, str):
            errors.append('manifest selection requires shot_id and take_id')
            continue
        selected_ids.append(sid)
        take = takes.get((sid, tid))
        if take is None:
            errors.append(f'manifest unknown take: {sid}/{tid}')
        elif take['status'] == 'rejected_editorial':
            errors.append(f'manifest selects rejected take: {sid}/{tid}')
        elif stage == 'edit' and take['file'] is None:
            errors.append(f'{sid}/{tid}: local clip required for edit')
    if len(set(selected_ids)) != len(selected_ids):
        errors.append('manifest duplicate selected shot')
    if selected_ids != [sid for sid in ids if sid in selected_ids]:
        errors.append('manifest selected shot order differs from episode')
    if stage == 'generation':
        expected = {'mode':'frames','agent':False,'model':'Veo 3.1 Lite','duration_seconds':8,'aspect_ratio':'9:16','outputs':1,'last_frame':None}
        if data['generation'] != expected:
            errors.append('generation must use Frames, Agent off, Veo 3.1 Lite, 8s, 9:16, one output, no last frame')
        if not data['flow_project']:
            errors.append('Flow project required for generation')
        if data['editorial_status'] == 'draft':
            errors.append('draft episode cannot pass generation gate')
    if stage == 'edit':
        if selected_ids != ids:
            errors.append('edit requires one selected take per shot in episode order')
        audio = manifest.get('audio_plan')
        if not isinstance(audio, dict):
            errors.append('structured audio_plan required')
        else:
            if audio.get('mute_veo_native') is not True or audio.get('engine') != 'VieNeu-TTS':
                errors.append('edit must mute Veo native audio and use VieNeu-TTS')
            if audio.get('voice_status') != 'locked' or not isinstance(audio.get('voice_preset'), str) or not audio['voice_preset'].strip():
                errors.append('voice preset pending: not ready to render dubbed edit')
            if 'lip_sync_qc' not in audio:
                errors.append('lip_sync_qc tracking required before edit')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('episode', type=Path)
    parser.add_argument('--stage', choices=['generation', 'edit'])
    args = parser.parse_args()
    try:
        errors = validate(args.episode, args.stage)
    except (OSError, ValueError, yaml.YAMLError) as error:
        errors = [str(error)]
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    if not errors:
        if args.stage:
            print(f'Offline {args.stage} checks passed; no Flow job submitted; media QC not certified.')
        else:
            print('Episode structure valid; generation/edit readiness and media QC not certified.')
            data = yaml.safe_load((args.episode / 'episode.yaml').read_text())
            for shot in data['shots']:
                if shot['first_frame'] is None:
                    print(f"NOTE: {shot['shot_id']}: local first frame missing")
                for take in shot['takes']:
                    if take['status'] != 'rejected_editorial' and take['file'] is None:
                        print(f"NOTE: {shot['shot_id']}/{take['take_id']}: local clip missing")
            manifest = yaml.safe_load((args.episode / 'edit/manifest.yaml').read_text())
            if manifest.get('audio_plan', {}).get('voice_status') != 'locked':
                print('NOTE: VieNeu voice pending user choice')
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())

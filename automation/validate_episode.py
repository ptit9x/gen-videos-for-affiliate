#!/usr/bin/env python3
"""Validate local episode input only; never contacts Flow or changes files."""
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
    sys.exit('Requires jsonschema and PyYAML; see automation/README.md')


def validate(episode):
    episode = episode.resolve()
    base = episode / 'input'
    errors = []
    schema = json.loads((Path(__file__).parent / 'schemas/shots.schema.json').read_text())
    data = json.loads((base / 'shots.json').read_text())
    for error in Draft202012Validator(schema).iter_errors(data):
        location = '/'.join(map(str, error.absolute_path)) or 'root'
        errors.append(f'{location}: {error.message}')
    if errors:
        return errors
    metadata = yaml.safe_load((episode / 'episode.yaml').read_text())
    if not isinstance(metadata, dict):
        return ['episode.yaml must be an object']
    for key in ('schema_version', 'episode_id', 'revision'):
        if metadata.get(key) != data[key]:
            errors.append(f'episode.yaml {key} differs from input')
    if metadata.get('input_file') != 'input/shots.json':
        errors.append('episode.yaml input_file must be input/shots.json')
    ids = [s['shot_id'] for s in data['shots']]
    if len(set(ids)) != len(ids):
        errors.append('duplicate shot_id')
    if metadata.get('shot_order') != ids:
        errors.append('episode.yaml shot_order differs from input')

    def asset(relative, expected_hash, prompt=False):
        parts = PurePosixPath(relative)
        if parts.is_absolute() or '..' in parts.parts or '\\' in relative or ':' in relative:
            errors.append(f'unsafe path: {relative}')
            return
        target = (base / relative).resolve()
        if not target.is_relative_to(base.resolve()) or not target.is_file():
            errors.append(f'missing or escaped asset: {relative}')
            return
        raw = target.read_bytes()
        if not raw:
            errors.append(f'empty asset: {relative}')
        if hashlib.sha256(raw).hexdigest() != expected_hash:
            errors.append(f'checksum mismatch: {relative}')
        if prompt:
            try:
                text = raw.decode('utf-8').strip()
            except UnicodeDecodeError:
                errors.append(f'prompt must be UTF-8: {relative}')
                return
            if not text or re.search(r'\[[^\]]+\]|\{\{|\b(?:TODO|TBD|DRAFT)\b', text, re.I):
                errors.append(f'empty or unresolved prompt: {relative}')

    for shot in data['shots']:
        asset(shot['prompt_file'], shot['prompt_sha256'], prompt=True)
        if set(shot['reference_files']) != set(shot['reference_sha256']):
            errors.append(f"{shot['shot_id']}: reference hash keys differ from files")
        for reference in shot['reference_files']:
            asset(reference, shot['reference_sha256'].get(reference))
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('episode', type=Path)
    args = parser.parse_args()
    try:
        errors = validate(args.episode)
    except (OSError, ValueError, yaml.YAMLError) as error:
        errors = [str(error)]
    for error in errors:
        print(f'ERROR: {error}', file=sys.stderr)
    if not errors:
        print('Input valid; no Flow job submitted.')
    return int(bool(errors))


if __name__ == '__main__':
    sys.exit(main())

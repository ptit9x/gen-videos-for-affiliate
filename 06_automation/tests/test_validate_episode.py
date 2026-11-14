import copy
import hashlib
import importlib.util
from pathlib import Path
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location('validator', ROOT / '06_automation/validate_episode.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class EpisodeValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.ep = Path(self.temp.name)
        self.data = yaml.safe_load((ROOT / '06_automation/tests/fixtures/draft-episode/episode.yaml').read_text())
        self.manifest = yaml.safe_load((ROOT / '06_automation/tests/fixtures/draft-episode/edit/manifest.yaml').read_text())
        self.shot = self.data['shots'][0]
        self.data.update(title='Test', editorial_status='script_approved', flow_project='https://flow.google.com/project/test')
        self.shot.update(approved_for_generation=True, dialogue='Chào bạn.', frame_status='approved')
        self.shot['image_prompt'] = self.asset('input/prompts/sh010-image.txt', b'Keep the same woman. Change the room.')
        self.shot['motion_prompt'] = self.asset('input/prompts/sh010-motion.txt', 'She nods and says “Chào bạn.” Static camera.'.encode())
        self.shot['image_sources'] = [self.asset('input/references/identity.png', b'identity-fixture')]
        self.shot['first_frame'] = self.asset('input/frames/sh010.png', b'scene-fixture')
        self.shot['takes'] = [{'take_id':'take001','clip_id':'test-id','status':'accepted_editorial','file':self.asset('generated/sh010/take001.mp4', b'clip-fixture'),'note':'Offline file checks only; media content not certified.'}]
        self.manifest['selected_takes'] = [{'shot_id':'sh010','take_id':'take001'}]
        self.manifest['audio_plan'].update(voice_preset='test-approved-preset', voice_status='locked')

    def asset(self, name, raw):
        path = self.ep / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw)
        return {'path':name,'sha256':hashlib.sha256(raw).hexdigest()}

    def check(self, stage=None):
        (self.ep / 'episode.yaml').write_text(yaml.safe_dump(self.data, allow_unicode=True))
        (self.ep / 'edit').mkdir(exist_ok=True)
        (self.ep / 'edit/manifest.yaml').write_text(yaml.safe_dump(self.manifest))
        return validator.validate(self.ep, stage)

    def test_valid_all_stages(self):
        for stage in (None, 'generation', 'edit'):
            self.assertEqual(self.check(stage), [])

    def test_missing_frame_only_blocks_generation(self):
        self.shot.update(first_frame=None, frame_status='missing_local')
        self.assertEqual(self.check(), [])
        self.assertTrue(any('local first frame' in e for e in self.check('generation')))

    def test_bad_hash(self):
        self.shot['motion_prompt']['sha256'] = '0' * 64
        self.assertTrue(any('checksum mismatch' in e for e in self.check()))

    def test_unsafe_and_symlink_paths(self):
        for path in ('../outside', '/tmp/outside', 'input\\outside', 'C:outside'):
            self.shot['first_frame']['path'] = path
            self.assertTrue(any('unsafe path' in e for e in self.check()))
        (self.ep / 'escape').symlink_to(ROOT / 'README.md')
        self.shot['first_frame']['path'] = 'escape'
        self.assertTrue(any('escaped asset' in e for e in self.check()))

    def test_duplicate_shot(self):
        self.data['shots'].append(copy.deepcopy(self.shot))
        self.assertTrue(any('duplicate shot_id' in e for e in self.check()))

    def test_manifest_revision_and_take(self):
        self.manifest['revision'] = 99
        self.manifest['selected_takes'][0]['take_id'] = 'take999'
        errors = self.check()
        self.assertTrue(any('revision' in e for e in errors))
        self.assertTrue(any('unknown take' in e for e in errors))

    def test_draft_template(self):
        template = ROOT / '06_automation/tests/fixtures/draft-episode'
        self.assertEqual(validator.validate(template), [])
        self.assertTrue(validator.validate(template, 'generation'))
        self.assertTrue(validator.validate(template, 'edit'))

    def test_missing_clip_and_voice(self):
        self.shot['takes'][0]['file'] = None
        self.manifest['audio_plan'].update(voice_preset=None, voice_status='pending_user_choice')
        self.assertEqual(self.check(), [])
        errors = self.check('edit')
        self.assertTrue(any('local clip required' in e for e in errors))
        self.assertTrue(any('voice preset pending' in e for e in errors))

    def test_generation_settings_and_legacy_payload(self):
        self.data['generation']['agent'] = True
        self.assertTrue(self.check('generation'))
        self.shot['reference_files'] = ['old.png']
        self.assertTrue(any('Additional properties' in e for e in self.check()))

    def test_identity_is_not_a_frame(self):
        self.shot['first_frame'] = copy.deepcopy(self.shot['image_sources'][0])
        self.assertTrue(any('cannot substitute' in e for e in self.check('generation')))

    def test_bad_prompt_and_missing_file(self):
        self.shot['motion_prompt'] = self.asset('input/prompts/sh010-motion.txt', b'\xff')
        self.assertTrue(any('UTF-8' in e for e in self.check()))
        self.shot['motion_prompt'] = self.asset('input/prompts/sh010-motion.txt', b'TODO: fill this')
        self.assertTrue(any('unresolved' in e for e in self.check()))
        (self.ep / self.shot['motion_prompt']['path']).unlink()
        self.assertTrue(any('missing or escaped' in e for e in self.check()))

    def test_rejected_take_and_duplicate_selection(self):
        self.shot['takes'][0]['status'] = 'rejected_editorial'
        self.manifest['selected_takes'] *= 2
        errors = self.check()
        self.assertTrue(any('rejected take' in e for e in errors))
        self.assertTrue(any('duplicate selected shot' in e for e in errors))


if __name__ == '__main__':
    unittest.main()

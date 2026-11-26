import contextlib
import io
from pathlib import Path
import tempfile
import unittest

from iso6346_validation_claim_audit.audit import audit, claims, evidence, main
from iso6346_validation_claim_audit.phrases import ISO6346VALIDATION, NOISO6346VALIDATION, GENERIC_NAMES


class AuditTests(unittest.TestCase):
    def test_phrases(self):
        self.assertEqual((len(ISO6346VALIDATION), len(NOISO6346VALIDATION), len(GENERIC_NAMES)), (50, 24, 24))
        for phrase in ISO6346VALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (True, False))
        for phrase in NOISO6346VALIDATION:
            with self.subTest(phrase=phrase):
                self.assertEqual(claims(phrase), (False, True))
        self.assertEqual(claims('```\nvalidate iso6346\n```\n~~~\nno iso6346 validation\n~~~'), (False, False))
        self.assertEqual(claims("doesn't validate-container number"), (False, True))
        self.assertEqual(claims('`validate iso 6346`'), (True, False))

    def test_library_routes(self):
        for method in ('validate', 'is_valid'):
            for source in ('import stdnum.iso6346\nstdnum.iso6346.%s(x)', 'import stdnum.iso6346 as s\ns.%s(x)', 'import stdnum\nstdnum.iso6346.%s(x)', 'from stdnum import iso6346 as s\ns.%s(x)', 'from stdnum.iso6346 import %s as f\nf(x)'):
                with self.subTest(source=source, method=method):
                    self.assertTrue(evidence(source % method))

    def test_generic_routes(self):
        for name in GENERIC_NAMES:
            with self.subTest(name=name):
                self.assertTrue(evidence('obj.%s(x)' % name))
                self.assertTrue(evidence('from lib import %s as f\nf(x)' % name))
                self.assertFalse(evidence('%s(x)' % name))
                self.assertFalse(evidence('def %s(x): pass\nobj.%s(x)' % (name, name)))
        self.assertTrue(evidence('result = thing()\nresult.validate_container_number(x)'))

    def test_not_evidence(self):
        cases = ['import stdnum.iso6346', 'iso6346(x)', 'validate(x)', 'is_valid(x)', 'compact(x)', 'calc_check_digit(x)', 'format(x)', 'validate_container_number(x)', 'obj.validate(x)', 'obj.is_valid(x)', 'obj.iso6346(x)', 'obj.compact(x)', 'obj.calc_check_digit(x)', 'obj.format(x)', 'import stdnum.iso6346\nstdnum.iso6346.compact(x)', 'import stdnum.iso6346\nstdnum.iso6346.calc_check_digit(x)', 'import stdnum.iso6346\nstdnum.iso6346.format(x)', 'import stdnum.isin\nstdnum.isin.validate(x)', 'import stdnum.isin\nstdnum.isin.is_valid(x)', 'import stdnum.isin\nstdnum.isin.from_natid(x)', 'import validators\nvalidators.isin(x)', 'obj.validate_sedol(x)', 'obj.validate_figi(x)', 'obj.validate_isni(x)', 'obj.validate_cusip(x)', 'import re\nre.match("x", x)', 'import re\nre.search("x", x)', 'import re\nre.fullmatch("x", x)', 'len(x) == 11', 'x[4] == " "', 'all(c in "ABC" for c in x)', 'x[3] in "UJZR"', 'x[:3].isalpha()', 'obj.lookup_container_number(x)', 'obj.generate_container_number()', '"validate container number"', '# container number validation', 'validate_container_number', 'def broken(', 'import subprocess\nsubprocess.run(["checker", x])', 'import stdnum.iso6346 as s\ns = x\ns.validate(x)', 'from stdnum.iso6346 import validate\ndef validate(x): pass\nvalidate(x)', 'import stdnum.iso6346 as s\nwith thing() as s: pass\ns.validate(x)', 'from stdnum.iso6346 import validate\nvalidate: object = x\nvalidate(x)']
        for source in cases:
            with self.subTest(source=source):
                self.assertFalse(evidence(source))

    def test_repository(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / 'README.md').write_text('validate container number')
            self.assertEqual(audit(root)[0]['severity'], 'HIGH')
            (root / 'tests').mkdir()
            (root / 'tests/test_x.py').write_text('import stdnum.iso6346\nstdnum.iso6346.validate(x)')
            self.assertEqual(audit(root)[0]['severity'], 'MEDIUM')
            (root / 'app.py').write_text('import stdnum.iso6346\nstdnum.iso6346.is_valid(x)')
            self.assertEqual(audit(root), [])
            (root / 'README.md').write_text('no container number validation')
            self.assertEqual(audit(root)[0]['id'], 'documented-no-iso6346-validation-claim-false')
            self.assertEqual(audit(root, ['app.py']), [])
            self.assertEqual(audit(root, ['app.py', 'tests']), [])
        project = Path(__file__).resolve().parents[1]
        self.assertEqual(audit(project), [])
        readme = (project / 'README.md').read_text()
        self.assertEqual(claims(readme), (False, False))
        for value in ('documented iso6346 validation claim false', 'iso6346 validation claim audit', 'documented no iso6346 validation claim false'):
            self.assertEqual(claims(value), (False, False))
        prose = []
        fenced = False
        for line in readme.splitlines():
            if line.startswith('```'):
                fenced = not fenced
            elif not fenced:
                prose.append(line)
        self.assertEqual(claims('\n'.join(prose)), (False, False))
        self.assertNotIn('the phrase', readme)
        self.assertNotIn('a tool that', readme)

    def test_cli(self):
        with tempfile.TemporaryDirectory() as tmp, contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            self.assertEqual(main(['audit', tmp, '--json']), 0)
            self.assertEqual(main(['audit', tmp, '--fail-on', 'medium']), 0)
            self.assertEqual(main(['audit', tmp + '/missing']), 1)
            Path(tmp, 'README.md').write_text('validate container number')
            self.assertEqual(main(['audit', tmp]), 2)

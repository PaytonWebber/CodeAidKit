import os
import unittest
import tempfile
import codeaidkit as cak


class TestPEP8(unittest.TestCase):

    def setUp(self):
        # Create a temporary file with Python code
        self.temp_file = tempfile.NamedTemporaryFile(
            mode='w+',
            suffix='.py',
            delete=False
        )
        self.temp_file.write("import os\n\n\n\nos.path.join('a', 'b')\n")
        self.temp_file.close()

    def tearDown(self):
        # Delete the temporary file
        os.unlink(self.temp_file.name)

    def test_check_pep8(self):
        issues = cak.check_pep8(self.temp_file.name)
        self.assertEqual(len(issues), 1)  # There should be one issue (E303)

    def test_chek_pep8_ignore(self):
        issues = cak.check_pep8(self.temp_file.name, ignore=['E303'])
        self.assertEqual(len(issues), 0)  # There should be no issues


if __name__ == '__main__':
    unittest.main()

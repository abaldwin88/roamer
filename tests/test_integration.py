"""
askldjf
"""
import os
import shutil
import unittest
import re
from roamer.main import Main
from roamer.constant import TEST_DIR

HELLO_DIR = os.path.join(TEST_DIR, 'hello/')
DOC_DIR = os.path.join(TEST_DIR, 'docs/')
SPAM_FILE = os.path.join(TEST_DIR, 'spam.txt')
EGG_FILE = os.path.join(TEST_DIR, 'egg.txt')
ARGH_FILE = os.path.join(TEST_DIR, 'argh.md')
RESEARCH_FILE = os.path.join(DOC_DIR, 'research.txt')

# TODO: stub out trash/entry constants

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DIR):
            shutil.rmtree(TEST_DIR)
        os.makedirs(TEST_DIR)

        os.makedirs(HELLO_DIR)
        os.makedirs(DOC_DIR)
        with open(SPAM_FILE, "w") as text_file:
            text_file.write('spam file content')
        with open(EGG_FILE, "w") as text_file:
            text_file.write('egg file content')
        with open(ARGH_FILE, "w") as text_file:
            text_file.write('argh file content')
        with open(RESEARCH_FILE, "w") as text_file:
            text_file.write('research file content')

        self.main = Main(TEST_DIR)
        self.text = self.main.directory.text()

    def process(self):
        self.main.process(self.text)

    def test_directory_text_output(self):
        self.assertTrue('hello/' in self.text)
        self.assertTrue('docs/' in self.text)
        self.assertTrue('spam.txt' in self.text)
        self.assertTrue('egg.txt' in self.text)
        self.assertTrue('argh.md' in self.text)

    def test_create_new_file(self):
        self.text += '\nnew_file.txt'
        self.process()
        path = os.path.join(TEST_DIR, 'new_file.txt')
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isfile(path))

    def test_create_new_directory(self):
        self.text += '\nnew_dir/'
        self.process()
        path = os.path.join(TEST_DIR, 'new_dir/')
        self.assertTrue(os.path.exists(path))
        self.assertTrue(os.path.isdir(path))

    def test_delete_file(self):
        self.text = re.sub(r'argh.md.*\n', '', self.text)
        self.process()
        self.assertFalse(os.path.exists(ARGH_FILE))

    def test_delete_directory(self):
        self.text = re.sub(r'hello\/.*\n', '', self.text)
        self.process()
        self.assertFalse(os.path.exists(HELLO_DIR))

    def test_copy_file(self):
        digest = re.search(r'egg.txt\ \|\ (.*)', self.text, re.MULTILINE).group(1)
        new_line = 'egg2.txt | %s' % digest
        self.text += '\n%s' % new_line
        self.process()
        path = os.path.join(TEST_DIR, 'egg2.txt')
        self.assertTrue(os.path.exists(path))
        with open(path, 'r') as egg2_file:
            self.assertEqual(egg2_file.read(), 'egg file content')

    def test_copy_directory(self):
        digest = re.search(r'docs\/\ \|\ (.*)', self.text, re.MULTILINE).group(1)
        new_line = 'docs2/ | %s' % digest
        self.text += '\n%s' % new_line
        self.process()
        path = os.path.join(TEST_DIR, 'docs2/')
        self.assertTrue(os.path.exists(path))
        contents = os.listdir(path)
        self.assertEqual(contents, ['research.txt'])

    def test_rename_file(self):
        self.text = re.sub(r'argh.md', 'blarg.md', self.text)
        self.process()
        self.assertFalse(os.path.exists(ARGH_FILE))
        path = os.path.join(TEST_DIR, 'blarg.md')
        self.assertTrue(os.path.exists(path))
        with open(path, 'r') as blarg_file:
            self.assertEqual(blarg_file.read(), 'argh file content')

    def test_rename_directory(self):
        self.text = re.sub(r'docs/', 'my-docs/', self.text)
        self.process()
        # TODO: multiple deletes fails here
        self.assertFalse(os.path.exists(DOC_DIR))
        path = os.path.join(TEST_DIR, 'my-docs/')
        self.assertTrue(os.path.exists(path))
        contents = os.listdir(path)
        self.assertEqual(contents, ['research.txt'])

    def test_rename_file_to_directory(self):
        self.text = re.sub(r'hello\/', 'hello.txt', self.text)
        with self.assertRaises(ValueError):
            self.process()

    def test_empty_lines(self):
        self.text += '\n    \n    \n '
        self.process()
        self.assertTrue(os.path.exists(ARGH_FILE))

if __name__ == '__main__':
    unittest.main()

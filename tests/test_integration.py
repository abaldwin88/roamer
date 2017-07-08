"""
askldjf
"""
import os
import shutil
import unittest
from roamer.main import Main
from roamer.constant import TEST_DIR

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        if os.path.exists(TEST_DIR):
            shutil.rmtree(TEST_DIR)
            os.makedirs(TEST_DIR)
        else:
            os.makedirs(TEST_DIR)

        os.makedirs(os.path.join(TEST_DIR, 'hello/'))
        with open(os.path.join(TEST_DIR, 'spam.txt'), "w") as text_file:
            text_file.write('spam file content')
        with open(os.path.join(TEST_DIR, 'eggs.txt'), "w") as text_file:
            text_file.write('eggs file content')
        with open(os.path.join(TEST_DIR, 'argh.txt'), "w") as text_file:
            text_file.write('argh file content')
        self.main = Main(TEST_DIR)
        self.text = self.main.directory.text()

    def process(self):
        self.main.process(self.text)

    def tearDown(self):
        shutil.rmtree(TEST_DIR)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()

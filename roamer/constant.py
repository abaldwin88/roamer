"""
App wide constants.
"""
import os
from os.path import expanduser, join, dirname, realpath, exists

ROAMER_DATA_PATH = os.environ.get('ROAMER_DATA_PATH') or expanduser('~/.roamer-data/')
ENTRIES_JSON_PATH = expanduser(join(ROAMER_DATA_PATH, 'entries.json'))
TRASH_JSON_PATH = expanduser(join(ROAMER_DATA_PATH, 'trash.json'))
TRASH_DIR = expanduser(join(ROAMER_DATA_PATH, 'trash/'))
TEST_DIR = expanduser(dirname(realpath(__file__)) + '/../tmp/test_dir/')

if not exists(TRASH_DIR):
    os.makedirs(TRASH_DIR)

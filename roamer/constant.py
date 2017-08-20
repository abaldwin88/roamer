"""
App wide constants.
"""
import os
from os.path import expanduser, join, exists

ROAMER_DATA_PATH = os.environ.get('ROAMER_DATA_PATH') or expanduser('~/.roamer-data/')
ROAMER_DATABASE = expanduser(join(ROAMER_DATA_PATH, 'roamer.db'))
TRASH_DIR = expanduser(join(ROAMER_DATA_PATH, 'trash/'))
TEST_DIR = expanduser(join(ROAMER_DATA_PATH, 'tmp/test/mock_dir'))

if not exists(TRASH_DIR):
    os.makedirs(TRASH_DIR)

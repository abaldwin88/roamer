"""
kldj
"""
import os

ENTRIES_JSON_PATH = os.path.expanduser('~/.roamer-data/entries.json')
TRASH_JSON_PATH = os.path.expanduser('~/.roamer-data/trash.json')
TRASH_DIR = os.path.expanduser('~/.roamer-data/trash/')
TEST_DIR = os.path.expanduser('~/lasdkfj/')

if not os.path.exists(TRASH_DIR):
    os.makedirs(TRASH_DIR)
if not os.path.exists(TEST_DIR):
    os.makedirs(TEST_DIR)

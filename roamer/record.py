"""
argh
"""
import os
import json
from roamer.entry import Entry
from roamer.constant import ENTRIES_JSON_PATH, TRASH_JSON_PATH, TRASH_DIR

class Record(object):
    def __init__(self):
        self.entries = self._load(ENTRIES_JSON_PATH)
        self.trash_entries = self._load(TRASH_JSON_PATH)

    @staticmethod
    def _load(path):
        dictionary = {}
        if os.path.exists(path):
            with open(path) as data_file:
                data = json.load(data_file)
            for digest, entry_data in data.iteritems():
                entry = Entry(entry_data['name'], entry_data['directory'], digest)
                dictionary[entry.digest] = entry
        return dictionary

    def add_dir(self, directory):
        with open(ENTRIES_JSON_PATH, 'w') as outfile:
            entries = {}
            for entry in directory.entries.values():
                entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
            json.dump(entries, outfile)

    def add_trash(self, digest, name):
        self.trash_entries[digest] = {'name': name, 'directory': TRASH_DIR}
        with open(TRASH_JSON_PATH, 'w') as outfile:
            json.dump(self.trash_entries, outfile)

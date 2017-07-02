"""
argh
"""
import os
import json
from roamer.entry import Entry

entries_path = os.path.expanduser('~/.roamer-data/entries.json')
trash_path = os.path.expanduser('~/.roamer-data/trash.json')

class Record(object):
    def __init__(self):
        self.entries = self._load(entries_path)
        self.trash_entries = self._load(trash_path)

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

    @staticmethod
    def add_dir(directory):
        # TODO: Create parent dirs if they don't exist
        with open(entries_path, 'w') as outfile:
            entries = {}
            for digest, entry in directory.entries.iteritems():
                entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
            json.dump(entries, outfile)

    @staticmethod
    def add_trash(digest, path):
        pass
        # TODO: add trash


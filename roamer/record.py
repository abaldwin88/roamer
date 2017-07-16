"""
Saves entries and their digests onto disk so they can be used in later sessions.
"""
import os
import json
from roamer.entry import Entry
from roamer.constant import ENTRIES_JSON_PATH, TRASH_JSON_PATH, TRASH_DIR
from roamer.directory import Directory

class Record(object):
    def __init__(self, filter_directory=None):
        self._filter_directory = filter_directory
        self.entries = self._load(ENTRIES_JSON_PATH)
        self.trash_entries = self._load(TRASH_JSON_PATH)

    def _load(self, path):
        dictionary = {}
        if os.path.exists(path):
            with open(path) as data_file:
                data = json.load(data_file)
            for digest, entry_data in data.iteritems():
                entry = Entry(entry_data['name'], Directory(entry_data['directory'], []), digest)
                if entry.directory != self._filter_directory:
                    dictionary[entry.digest] = entry
        return dictionary

    def add_dir(self, directory):
        entries = {}
        for entry in self.entries.values():
            if entry.directory != directory:
                entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
        for entry in directory.entries.values():
            entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
        with open(ENTRIES_JSON_PATH, 'w') as outfile:
            json.dump(entries, outfile)

    def add_trash(self, digest, name, directory):
        entries = {}
        for entry in self.trash_entries.values():
            entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
        entries[digest] = {'name': name, 'directory': directory}
        with open(TRASH_JSON_PATH, 'w') as outfile:
            json.dump(entries, outfile)

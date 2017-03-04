"""
argh
"""
import os
import json
from roamer.entry import Entry

entries_path = os.path.expanduser('~/.roamer-data/entries.json')

class Record(object):
    def __init__(self):
        self.entries = {}
        # TODO: Load saved directory json
        if os.path.exists(entries_path):
            with open(entries_path) as data_file:
                data = json.load(data_file)
            for digest, entry_data in data.iteritems():
                entry = Entry(entry_data['name'], entry_data['directory'], digest)
                self.entries[entry.digest] = entry
        # TODO: load trash json

    def add_dir(self, directory):
        # TODO: Create parent dirs if they don't exist

        with open(entries_path, 'w') as outfile:
            entries = {}
            for digest, entry in directory.entries.iteritems():
                entries[entry.digest] = {'name': entry.name, 'directory': entry.directory.path}
            json.dump(entries, outfile)


    def add_trash(self, path, digest):
        pass
        # TODO: add trash

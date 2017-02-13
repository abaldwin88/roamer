"""
argh
"""
from roamer.entry import Entry

class Directory(object):
    """
    argh
    """
    def __init__(self, path, raw_entries):
        self.path = path
        self.entries = {}
        for raw_entry in raw_entries:
            entry = Entry(raw_entry, self)
            self.entries[entry.digest] = entry

    def __str__(self):
        return self.path

    def text(self):
        content = []
        for entry in self.entries.itervalues():
            content.append(str(entry))
        return '\n'.join(content)

    def search(self, digest):
        return self.entries[digest]


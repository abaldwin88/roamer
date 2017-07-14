"""
Represents the original directory before any changes have been made.
"""
from roamer.entry import Entry

class Directory(object):
    def __init__(self, path, raw_entries):
        self.path = path
        self.entries = {}
        for raw_entry in raw_entries:
            entry = Entry(raw_entry, self)
            self.entries[entry.digest] = entry

    def __str__(self):
        return self.path

    def __eq__(self, other):
        if other is None:
            return False
        return self.path == other.path

    def __ne__(self, other):
        return not self.__eq__(other)

    def text(self):
        content = []
        for entry in self.entries.itervalues():
            content.append(str(entry))
        return '\n'.join(content)

    def find(self, digest):
        return self.entries.get(digest)

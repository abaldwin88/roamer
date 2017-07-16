"""
Represents a directory after the user has submitted edits
"""
from collections import Counter
from roamer.entry import Entry

class EditDirectory(object):
    def __init__(self, path, content):
        self.path = path
        self.entries = {}
        self.process_lines(content)
        self.handle_duplicate_names()

    def process_lines(self, content):
        for line in content.splitlines():
            name, digest = process_line(line)
            if name is None:
                continue
            entry = Entry(name, self.path, digest)
            if digest in self.entries:
                self.entries[digest].append(entry)
            else:
                self.entries[digest] = [entry]

    def handle_duplicate_names(self):
        for entries in self.entries.values():
            entry_names = [entry.name for entry in entries]
            entry_counts = Counter(entry_names)
            for entry_name, count in entry_counts.iteritems():
                for i in range(count - 1):
                    duplicate_entry = next(entry for entry in entries if entry.name == entry_name)
                    duplicate_entry.append_to_name('_copy_%s' % str(i + 1))

    def find(self, digest):
        return self.entries.get(digest)


def process_line(line):
    columns = line.split('|')
    name = columns[0]
    if name.isspace() or name == '':
        name = None
    elif name[-1] == ' ':
        name = name[:-1]

    if len(columns) == 1:
        digest = None
    else:
        digest = columns[1].replace(' ', '')
        if digest == '':
            digest = None
    return name, digest

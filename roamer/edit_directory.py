
"""
argh
"""
from roamer.entry import Entry

class EditDirectory(object):
    """
    argh
    """
    def __init__(self, path, content):
        self.path = path
        self.entries = {}

        for line in content.splitlines():
            name, digest = process_line(line)
            if name is None:
                continue
            entry = Entry(name, path, digest)
            if digest in self.entries:
                self.entries[digest].append(entry)
            else:
                self.entries[digest] = [entry]

    def find(self, digest):
        return self.entries.get(digest)


def process_line(line):
    columns = line.split('|')
    name = columns[0]
    if name[-1] == ' ':
        name = name[:-1]
    if name.isspace() or name == '':
        name = None

    if len(columns) == 1:
        digest = None
    else:
        digest = columns[1].replace(' ', '')
        if digest == '':
            digest = None
    return name, digest

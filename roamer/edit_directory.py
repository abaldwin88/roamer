
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
            entry = Entry(name, self, digest)
            self.entries[digest] = entry


def process_line(line):
    columns = line.split('|')
    name = columns[0]
    if name[-1] == ' ':
        name = name[:-1]

    if len(columns) == 1:
        digest = None
    digest = columns[1].replace(' ', '')
    if digest == '':
        digest = None
    return name, digest

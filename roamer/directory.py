"""
argh
"""
from roamer.entry import RoamerEntry

class RoamerDirectory(object):
    """
    argh
    """
    def __init__(self, directory, raw_entries):
        self.directory = directory
        self.searched_entries = []
        self.entries = {}
        for raw_entry in raw_entries:
            entry = RoamerEntry(raw_entry, self)
            self.entries[entry.digest] = entry

    def __str__(self):
        return self.directory

    def text(self):
        content = []
        for entry in self.entries.itervalues():
            content.append(str(entry))
        return '\n'.join(content)

    def search(self, digest):
        self.searched_entries.append(digest)
        return self.entries[digest]

    def process_edit(self, content):
        for line in content.splitlines():
            column = line.split('|')
            if len(column) == 1:
                return # new file
            digest = column[1].replace(' ', '')
            name = column
            if digest == '':
                return # new file
            if name[-1] == ' ':
                name = name[:-1]


            if digest in self.entries:
                entry = self.search(digest)
                if entry == name:
                    return # dont do anything
                else:
                    return # mv file

            raise Exception('Hash not found')

        missing_entries = list(set(self.searched_entries) - set(self.entries.keys))

        for entry in missing_entries:
            pass # delete entry


            """
            digest not searched for = rm
            find digest but name doesnt match  = copy from digest location to file(mv)
            find digest and name match = do nothing
            empty digest = touch new_file
            not find digest = error
            #####################

            file name ends in / then is dir
            """

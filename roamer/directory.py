import os
import hashlib

class EntryCollection(object):
    """
    argh
    """
    def __init__(self, directory, raw_entries):
        self.directory = directory
        self.searched_entries = []
        self.entries = {}
        self.digests = {}
        for entry in raw_entries:
            entry_path = os.path.join(self.directory, entry)
            full_digest = hashlib.sha224(entry_path).hexdigest()
            digest = full_digest[0:7]
            # if digest in self.digests:
                # raise Exception('Duplicate hash digest')
            self.digests[digest] = full_digest
            self.entries[digest] = entry

    def text(self):
        content = []
        for digest, entry in self.entries.iteritems():
            string = "%s | %s" % (entry, digest)
            content.append(string)
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

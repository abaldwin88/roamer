"""
argh
"""
import os

class Command(object):
    def __init__(self, cmd, first_entry, second_entry=None):
        if cmd not in ('cp', 'rm', 'mv', 'touch'):
            raise 'Invalid command'
        self.cmd = cmd
        self.first_entry = first_entry
        self.second_entry = second_entry
        # TODO: Modify switches based on whether entry is a directory
        self.options = None


    def __str__(self):
        second_path = None
        if self.second_entry:
            second_path = self.second_entry.path
        parts = filter(None, (self.cmd, self.options, self.first_entry.path, second_path))
        return ' '.join(parts)

    def execute(self):
        if self.cmd == 'rm':
            self.cmd = 'mv'
            self.second_entry = Entry(first_entry.name, TRASH_DIR, first_entry.digest)
            record.add_trash(first_entry.digest, second_entry.path)

        print str(self)
        os.system(str(self))

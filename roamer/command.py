"""
Represents a single os command
"""
import os
from roamer.entry import Entry
from roamer.record import Record
from roamer.constant import TRASH_DIR

COMMAND_ORDER = {'touch': 1, 'roamer-trash-copy': 2, 'cp': 3, 'rm': 4}

class Command(object):
    def __init__(self, cmd, first_entry, second_entry=None):
        if cmd not in ('touch', 'roamer-trash-copy', 'cp', 'rm'):
            raise ValueError('Invalid command')
        if first_entry.__class__ != Entry:
            raise TypeError('first_entry not of type Entry')
        if second_entry.__class__ != Entry and second_entry != None:
            raise TypeError('second_entry not of type Entry or None')
        self.cmd = cmd
        self.first_entry = first_entry
        self.second_entry = second_entry
        self.options = None
        if self.first_entry.is_dir():
            if cmd == 'touch':
                self.cmd = 'mkdir'
            elif cmd == 'rm':
                self.options = '-R'
            elif cmd == 'roamer-trash-copy':
                pass
            elif not self.second_entry.is_dir():
                raise ValueError('Directories and Files cannot be interchanged.  ' \
                                 'Trailing slash (/) designates a directory.')
            elif cmd == 'cp':
                self.options = '-R'


    def __str__(self):
        second_path = None
        if self.second_entry:
            second_path = self.second_entry.path
        parts = filter(None, (self.cmd, self.options, self.first_entry.path, second_path))
        return ' '.join(parts)

    def __lt__(self, other):
        return self.order_int() < other.order_int()

    def order_int(self):
        return COMMAND_ORDER[self.cmd]

    def execute(self):
        if self.cmd == 'roamer-trash-copy':
            self.cmd = 'cp'
            trash_entry_dir = os.path.join(TRASH_DIR, self.first_entry.digest)
            self.second_entry = Entry(self.first_entry.name, trash_entry_dir,
                                      self.first_entry.digest)
            if  self.second_entry.persisted():
                if self.second_entry.is_dir():
                    os.system('rm -R %s' % self.second_entry.path)
                else:
                    os.system('rm %s' % self.second_entry.path)
            if not os.path.exists(trash_entry_dir):
                os.makedirs(trash_entry_dir)

            Record().add_trash(self.first_entry.digest, self.second_entry.name, trash_entry_dir)
        os.system(str(self))

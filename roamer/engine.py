"""
argh
"""
from roamer.command import Command
from roamer.record import Record
from roamer.entry import Entry

class Engine(object):
    def __init__(self, original_dir, edit_dir):
        self.commands = []
        for digest, original_entry in original_dir.entries.iteritems():
            new_entries = edit_dir.find(digest)
            if new_entries is None:
                self.commands.append(Command('roamer-trash', original_entry))
                continue
            found_original = False
            for new_entry in new_entries:
                if new_entry.name == original_entry.name:
                    found_original = True
                else:
                    self.commands.append(Command('cp', original_entry, new_entry))
            if not found_original:
                self.commands.append(Command('roamer-trash', original_entry))

        add_blank_entries = edit_dir.find(None)
        if add_blank_entries:
            for entry in add_blank_entries:
                self.commands.append(Command('touch', entry))

        unknown_digets = set(edit_dir.entries.keys()) - set(original_dir.entries.keys())

        for digest in filter(None, unknown_digets):
            record = Record(original_dir)
            outside_entry = record.entries.get(digest) or record.trash_entries.get(digest)
            if outside_entry is None:
                raise Exception('digest %s not found' % digest)
            new_entry = Entry(outside_entry.name, original_dir)
            self.commands.append(Command('cp', outside_entry, new_entry))

    def print_commands(self):
        string_commands = [str(command) for command in sorted(self.commands)]
        # sort so that cp comes first.  Need to copy before removals happen
        return '\n'.join(string_commands)

    def run_commands(self):
        return [command.execute() for command in sorted(self.commands)]

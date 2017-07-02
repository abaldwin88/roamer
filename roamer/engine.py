"""
argh
"""
from roamer.command import Command

class Engine(object):
    def __init__(self, original_dir, edit_dir, record):
        self.commands = []
        copied_entries = []
        for digest, original_entry in original_dir.entries.iteritems():
            new_entries = edit_dir.find(digest)
            if new_entries is None:
                # TODO: move to trash dir and add to record
                self.commands.append(Command('rm', original_entry))
                continue
            found_original = False
            for new_entry in new_entries:
                if new_entry.name == original_entry.name:
                    found_original = True
                else:
                    self.commands.append(Command('cp', original_entry, new_entry))
            if not found_original:
                self.commands.append(Command('rm', original_entry))

        for digest, entry in edit_dir.entries.iteritems():
            if digest is None:
                self.commands.append(Command('touch', entry))

        unknown_digets = set(edit_dir.entries.keys()) - set(original_dir.entries.keys())

        for digest in unknown_digets:
            # TODO: search record directory and trash
            if digest is not None:
                raise Exception('digest %s not found' % digest)

    def print_commands(self):
        # sort so that cp comes first.  Need to copy before removals happen
        if self.commands == []:
            return ''
        cmds = [str(cmd) for cmd in self.commands]
        # Commands being in alphabetical order just happen to be the order we want to execute
        return '\n'.join(sorted(cmds))

    def run_commands(self):
        raise
        return [cmd.execute for cmd in self.commands]




            # original --> compare to new
            # digets found same name = nothing
            # digest found new name = mv
            # empty digest = new
            # digest missing... rm


            # """
            # digest not searched for = rm
            # find digest but name doesnt match  = copy from digest location to file(mv)
            # find digest and name match = do nothing
            # empty digest = touch new_file
            # not find digest = error
            # #####################

            # file name ends in / then is dir
            # """

"""
argh
"""
class Engine(object):
    def __init__(self, original_dir, edit_dir):
        self.commands = []
        for digest, original_entry in original_dir.entries.iteritems():
            new_entry = edit_dir.find(digest)
            if new_entry is None:
                self.commands.append('rm %s' % original_entry.name)
            elif new_entry.name == original_entry.name:
                pass
            else:
                self.commands.append('mv %s %s' % original_entry.name, new_entry.name)

        for digest, entry in edit_dir.entries.iteritems():
            if digest is None:
                self.commands.append('touch %s %s' % entry.name)

        unknown_digets = set(edit_dir.entries.keys()) - set(original_dir.entries.keys())

        for digest in unknown_digets:
            raise Exception('digest %s not found' % digest)

    def print_commands(self):
        return ','.join(self.commands)





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

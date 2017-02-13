def process_edit(self, content):
    return
# for line in content.splitlines():
            # column = line.split('|')
            # if len(column) == 1:
                # return # new file
            # digest = column[1].replace(' ', '')
            # name = column
            # if digest == '':
                # return # new file
            # if name[-1] == ' ':
                # name = name[:-1]


            # if digest in self.entries:
                # entry = self.search(digest)
                # if entry == name:
                    # return # dont do anything
                # else:
                    # return # mv file

            # raise Exception('Hash not found')

        # missing_entries = list(set(self.searched_entries) - set(self.entries.keys))

        # for entry in missing_entries:
            # pass # delete entry


            # """
            # digest not searched for = rm
            # find digest but name doesnt match  = copy from digest location to file(mv)
            # find digest and name match = do nothing
            # empty digest = touch new_file
            # not find digest = error
            # #####################

            # file name ends in / then is dir
            # """

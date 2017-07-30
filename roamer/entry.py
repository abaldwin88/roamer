"""
Represents a single entry from the operating system.  Either a file or a directory.
"""

import os
import sys
import hashlib

class Entry(object):
    """
    argh
    """
    def __init__(self, name, directory, digest=None):
        self.directory = directory
        self.name = name
        self.set_path()
        if self.name and self.name[0] == '"':
            raise TypeError('roamer does not like files that start with # ')
        if os.path.isdir(self.path) and name[-1] != '/':
            self.name = name + '/'
        if digest:
            self.digest = digest
        else:
            if self.persisted():
                digest_text = self.path + str(os.path.getmtime(self.path))
            else:
                digest_text = self.path
            if sys.version_info[0] == 3:
                digest_text = digest_text.encode('utf-8')
            self.full_digest = hashlib.sha224(digest_text).hexdigest()
            self.digest = self.full_digest[0:12]

    def __str__(self):
        return "%s | %s" % (self.name, self.digest)

    def set_path(self):
        self.path = os.path.join(str(self.directory), self.name)

    def append_to_name(self, text):
        self.name = self.base_name() + text + self.extension()
        self.set_path()

    def is_dir(self):
        return self.name[-1] == '/'

    def persisted(self):
        return os.path.exists(self.path)

    def base_name(self):
        extension_length = len(self.extension())
        if extension_length == 0:
            return self.name
        return self.name[:-extension_length]

    def extension(self):
        if self.is_dir():
            return '/'
        return os.path.splitext(self.name)[1]

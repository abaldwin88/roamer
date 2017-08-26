"""
Represents a single entry from the operating system.  Either a file or a directory.
"""

import os
import sys
import hashlib
from roamer import record

class Entry(object):
    """
    argh
    """
    def __init__(self, name, directory, digest=None):
        self.directory = directory
        self.name = name
        self._set_path()
        if self.name and self.name[0] == '"':
            raise TypeError('Unexpected double quote ( " )')
        if os.path.isdir(self.path) and name[-1] != '/':
            self.name = name + '/'
        self.digest = digest
        if digest is None and self.persisted():
            self._set_version()
            digest_text = self.path + str(self.version)
            if sys.version_info[0] == 3 and digest_text:
                digest_text = digest_text.encode('utf-8')
            self.full_digest = hashlib.sha224(digest_text).hexdigest()
            self.digest = self.full_digest[0:12]

    def __str__(self):
        return "%s | %s" % (self.name, self.digest)

    def _set_path(self):
        self.path = os.path.join(str(self.directory), self.name)

    def _set_version(self):
        self.version = record.get_version(self.path, self.name)
        if self.version is None and self.persisted():
            self.version = int(os.path.getmtime(self.path))
            record.set_version(self.path, self.name, self.version)

    def increment_version(self):
        self._set_version()
        if self.version:
            self.version += 1
            record.set_version(self.path, self.name, self.version)

    def append_to_name(self, text):
        self.name = self.base_name() + text + self.extension()
        self._set_path()

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

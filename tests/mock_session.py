"""
Mocks a roamer session for testing purposes.
Wraps the session process to avoid actually interacting with a text editor.
Instead the text output that is normally destined for the users editor is available
for manipulation inside the tests.
"""
import re
from roamer.session import Session

class MockSession(object):
    def __init__(self, directory):
        self.load(directory)

    def load(self, directory):
        self.directory = directory
        self.session = Session(directory)
        self.text = self.session.directory.text()

    def reload(self):
        self.load(self.directory)

    def process(self):
        self.session.process(self.text)

    def add_entry(self, name, digest=None):
        if digest:
            new_line = '%s | %s' % (name, digest)
            self.text += '\n%s' % new_line
        else:
            self.text += '\n%s' % name

    def remove_entry(self, name):
        self.text = re.sub(r'%s.*\n?' % name, '', self.text, flags=re.MULTILINE)

    def get_digest(self, name):
        return re.search(r'%s\ \|\ (.*)' % name, self.text, re.MULTILINE).group(1)

    def rename(self, old_name, new_name):
        self.text = re.sub(old_name, new_name, self.text)

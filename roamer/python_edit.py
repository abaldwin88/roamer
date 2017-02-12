"""
argh
"""

import tempfile
import os
from subprocess import call

EDITOR = os.environ.get('EDITOR', 'vim')

if EDITOR in ['vim', 'nvim']:
    EXTRA_EDITOR_COMMAND = '+set backupcopy=yes'
else:
    EXTRA_EDITOR_COMMAND = None


def file_editor(content):
    with tempfile.NamedTemporaryFile(suffix=".tmp") as temp:
        temp.write(content)
        temp.flush()
        if EXTRA_EDITOR_COMMAND:
            call([EDITOR, EXTRA_EDITOR_COMMAND, temp.name])
        else:
            call([EDITOR, temp.name])
        temp.seek(0)
        return temp.read()

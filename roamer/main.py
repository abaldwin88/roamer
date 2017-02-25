#!/usr/bin/env python

"""
argh
"""

import os
from roamer.python_edit import file_editor
from roamer.directory import Directory
from roamer.edit_directory import EditDirectory
from roamer.engine import Engine


def main():
    """
    argh
    """
    cwd = os.getcwd()
    raw_entries = os.listdir(cwd)
    directory = Directory(cwd, raw_entries)
    output = file_editor(directory.text())
    edit_directory = EditDirectory(cwd, output)
    diff_engine = Engine(directory, edit_directory)
    print diff_engine.print_commands()

if __name__ == "__main__":
    main()

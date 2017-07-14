#!/usr/bin/env python

"""
This module is the entry point for the application.
"""

import os
from roamer.python_edit import file_editor
from roamer.directory import Directory
from roamer.edit_directory import EditDirectory
from roamer.engine import Engine
from roamer.record import Record

class Main(object):
    def __init__(self, cwd=None):
        self.cwd = cwd
        if cwd is None:
            self.cwd = os.getcwd()
        raw_entries = os.listdir(self.cwd)
        self.directory = Directory(self.cwd, raw_entries)
        self.edit_directory = None
        Record().add_dir(self.directory)

    def run(self):
        output = file_editor(self.directory.text())
        self.process(output)

    def process(self, output):
        self.edit_directory = EditDirectory(self.cwd, output)
        engine = Engine(self.directory, self.edit_directory)
        print engine.print_commands()
        engine.run_commands()
        Record().add_dir(Directory(self.cwd, os.listdir(self.cwd)))

if __name__ == "__main__":
    Main().run()

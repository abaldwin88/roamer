"""
This module is the entry point for the application.
Process command line arguments and pass appropriate flags to Session
"""

from __future__ import print_function
import sys
import roamer
from roamer.session import Session

def start(argv):
    skipapproval = False
    path = None
    if '--path' in argv:
        i = argv.index('--path') + 1
        path = argv[i]
    if '--version' in argv:
        return print(roamer.__version__)
    if '--raw-out' in argv:
        return Session(cwd=path).print_raw()
    if '--raw-in' in argv:
        return Session(cwd=path).process(sys.stdin.read())
    if '--skip-approval' in argv:
        skipapproval = True
    Session(cwd=path, skipapproval=skipapproval).run()

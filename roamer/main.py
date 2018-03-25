"""
This module is the entry point for the application.
Process command line arguments and pass appropriate flags to Session
"""

from __future__ import print_function
import sys
import pkg_resources
from roamer.session import Session

def start(argv):
    skipapproval = False
    if '--version' in argv:
        version = pkg_resources.require('roamer')[0].version
        print(version)
        return
    if '--raw-out' in argv:
        return Session().print_raw()
    if '--raw-in' in argv:
        return Session().process(sys.stdin.read())
    if '--skip-approval' in argv:
        skipapproval = True
    Session(skipapproval=skipapproval).run()

"""
This module is the entry point for the application.
Process command line arguments and pass appropriate flags to Session
"""

from __future__ import print_function
import sys

import click

import roamer
from roamer.session import Session


@click.command()
@click.option("--path", type=click.Path(file_okay=False, exists=True), default=None)
@click.option("--raw-out/--no-raw-out", default=False)
@click.option("--raw-in/--no-raw-in", default=False)
@click.option("--skip-approval/--no-skip-approval", "skipapproval", default=False)
@click.option("--version/--no-version", default=False)
def start(path, raw_out, raw_in, skipapproval, version):
    if version:
        print(roamer.__version__)
        return

    # TODO: Is this a bug? If --raw-out/in is specified, then --skip-approval is ignored.
    # Is that correct? For now, to remain backwards compatible I am maintaining this behaviour.
    if raw_out:
        Session(cwd=path).print_raw()
        return

    if raw_in:
        Session(cwd=path).process(sys.stdin.read())
        return

    Session(cwd=path, skipapproval=skipapproval).run()


if __name__ == "__main__":
    # It looks like we are calling start without providing any of the required
    # arguments, but actually it's fine due to the click decorators.
    # pylint doesn't know this though, so we tell it to ignore the call:
    # pylint: disable=no-value-for-parameter
    start()

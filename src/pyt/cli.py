"""
Module that contains the command line app.


  Also see (1) from http://click.pocoo.org/5/setuptools/#setuptools-integration
"""

# ---------------------------------------------------------------------
# Core Modules
import logging
import os

# ---------------------------------------------------------------------
# External Modules
import click

# ---------------------------------------------------------------------
# Internal Modules
from .lib.customLog import setup as logSetup
from .lib.customLog import log_with

log = logging.getLogger(__name__)


def initialize(debug):
    """ Set me up """
    if debug:
        os.environ['DEBUG'] = '1'
        logSetup(logging.INFO)

@click.command()
@click.version_option()
@click.option('-v', '--verbose', count=True)
@click.option('--debug/--no-debug', default=False, envvar='DEBUG')
@click.argument('names', nargs=-1)
def main(verbose, debug, names):
    """ Main method invoked from CLI """
    initialize(debug)

    echome(names)
    # click.echo("hello")
    # see
    # https://www.brianthicks.com/post/2014/11/03/build-modular-command-line-tools-with-click/


@log_with()
def echome(names):
    click.echo(repr(names))

"""
config.py: Contains Config class used to parse the config file.
"""

# ---------------------------------------------------------------------
# Core Modules
import py
import logging

# ---------------------------------------------------------------------
# External Modules
import click

# ---------------------------------------------------------------------
# Internal Modules

logger = logging.getLogger(__name__)


class Config(dict):
    def __init__(self, *args, **kwargs):
        self.config = py.path.local(
            click.get_app_dir('pyt')
        ).join('conf')
        super(Config, self).__init__(*args, **kwargs)

    def load(self):

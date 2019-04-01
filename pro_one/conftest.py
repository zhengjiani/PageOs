import os
import pytest
from __future__ import absolute_import, unicode_literals
REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), './failed_screenshots'))
REPO_ROOT1 = os.path.abspath(os.path.join(os.path.dirname(__file__), './source_html'))

def pytest_configure(config):  # pylint: disable=unused-argument
    """Set some environment variables to default values if absent"""
    if 'SCREENSHOT_DIR' not in os.environ:
        os.environ['SCREENSHOT_DIR'] =REPO_ROOT
    if 'SAVED_SOURCE_DIR' not in os.environ:
        os.environ['SAVED_SOURCE_DIR'] = REPO_ROOT1



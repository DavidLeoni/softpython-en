import sys
sys.path.append('../')
sys.path.append('.')  # good lord, without this debugging in VSCode doesn't work
#keep it first so we don't get deprecation warnings
import jupman_tools as jmt

from hypothesis import given
from hypothesis.strategies import text
from jupman_tools import tag_regex, Jupman
import pytest 
import re
from sphinx.application import Sphinx
import os
import nbformat

from common_test import *


#import exam
import shutil

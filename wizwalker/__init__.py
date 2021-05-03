import logging

from loguru import logger

from .constants import *
from .file_readers import Wad, NifMap
from .errors import *
from .utils import XYZ
from . import utils, cli, memory, combat
from .mouse_handler import MouseHandler
from .cache_handler import CacheHandler
from .client import Client
from .application import WizWalker

logger.disable("wizwalker")
# TODO: pr fixing this
logging.getLogger("pymem").setLevel(logging.FATAL)

"""Module with cosntant global values"""

from pathlib import Path

UTILITIES_DIR = Path(__file__).parent.absolute()
PROJECT_DIR = UTILITIES_DIR.parent
LOG_OUTPUT_DIR = Path(PROJECT_DIR, 'Output')

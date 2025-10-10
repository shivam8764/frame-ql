"""
FrameQL: A lightweight DataFrame library.
"""

# Makes the DataFrame class available when importing 'frame_ql'
# e.g., from frame_ql import DataFrame
from .frame import DataFrame

# Makes the read_csv function available
# e.g., from frame_ql import read_csv
from .io import read_csv

__version__ = "0.1.0"

# initialize module version

import os
from pathlib import Path

pardir = Path(__file__).parents[0]
file_path = os.path.join(pardir, "version_.py")

__version__ = None
exec(open(file_path).read())

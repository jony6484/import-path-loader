#### A setup for the test file
import sys
from pathlib import Path
sys.path.append(str((Path(__file__) / "../../..").resolve()))
####
from import_path_loader.path_loader import load_pths

load_pths("/home/jonaf/projects/import-path-loader/tests/.pth")

from testing_module import some_function, SOME_CONSTANT

from testing_module2 import some_function2, SOME_CONSTANT2
print('done')
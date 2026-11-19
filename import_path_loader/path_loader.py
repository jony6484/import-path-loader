import sys
import os
from pathlib import Path
import inspect

def load_pth_file(path: os.PathLike[str]):
    lines = []
    with open(path, "r") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                lines.append(line)
    return lines

def load_pths(path: os.PathLike[str]):
    paths = load_pth_file(path)
    caller_file = Path(inspect.stack()[1].filename).resolve()
    for path in paths:
        path = Path(path)
        if not path.is_absolute():
            path = (caller_file.parent / path).resolve()
        else:
            path = path.resolve()
        sys.path.append(str(path))
# import-path-loader

Load directories listed in a `.pth` file into Python's `sys.path`.

```python
from import_path_loader import load_pths

load_pths("paths.pth")
```

Non-empty lines and lines not starting with `#` are loaded. Relative entries
are resolved from the directory of the calling Python file; absolute entries
are used as-is.

## Build a wheel

Install the build frontend and create the wheel:

```sh
python -m pip install build
python -m build --wheel
```

The wheel is written to `dist/`. Install it with
`python -m pip install dist/import_path_loader-0.1.0-py3-none-any.whl`.
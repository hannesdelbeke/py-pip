# py-pip
A Python wrapper for `pip.exe` that passes env vars to pip.
Install packages from inside Python.

### Features
- pass env vars so pip can detect installed modules in different locations (e.g. Blender dynamicaly changes the Python path on startup)
- use pip from within Python, using the active interpreter

### Instructions
```python
import py_pip

# print all commands
[print(x) for x in dir(py_pip)]

# install numpy
py_pip.install("numpy")
```

### similar
- https://github.com/aescarias/pypiwrap
- https://pypi.org/project/pip-api/

### used by
- [pip-qt](https://github.com/hannesdelbeke/pip-qt)

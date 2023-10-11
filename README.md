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

### use case
Blender doesn't has an external Python interpreter.   
To use pip and have it correctly detect the installed modules:
- you need to run it from inside Blender.
- or recreate the environment, with same Python version and Python paths.

Else you might install a module that is already by default installed in Blender, because pip failed to detect it.  
This can result in clashes and weird bugs.  

This might (untested) also be achievable by passing `sys.path` to `os.environ["PYTHONPATH"]` and then running one of the below "similar" pip wrappers

### similar
Python pip wrappers, but without passing EnvPaths.

- https://github.com/aescarias/pypiwrap
- https://pypi.org/project/pip-api/

### used by
- [pip-qt](https://github.com/hannesdelbeke/pip-qt)

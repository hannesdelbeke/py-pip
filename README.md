# py-pip ![PyPI - Version](https://img.shields.io/pypi/v/py-pip)

Install Python packages, from inside a Python environment. e.g. in Blender, Maya, Max, ...   
  
The difference with similar solutions: py-pip passes it's sys.paths to pip, to support dynamicly added paths for e.g. Maya, Blender, ...  
(Otherwise any python paths added after startup wont be detected by pip, so it can't uninstall certain installed packages, or it might install an already installed package)  

### Features
- pass env vars so pip can detect installed modules in different locations (e.g. Blender dynamicaly changes the Python path on startup)  
  & handle env vars, to prevent non sys.path paths being passed.
- use pip from within Python, using the active interpreter

### Instructions
```python
import py_pip

# optional
py_pip.default_target_path = "C:/path/to/site-packages"  # defaults to no target path
py_pip.python_interpreter = "C:/path/to/python.exe"  # defaults to sys.executable

# the core commands
py_pip.install("dummy_test")  # install dummy_test
py_pip.uninstall("dummy_test")  # uninstall the dummy_test package
```

### use case
Blender doesn't has an external Python interpreter that sets up the Blender environment (Maya has `mayapy.exe`).   
To use pip and have it correctly detect the installed modules:
- you need to run it from inside Blender.
- or recreate the environment, with same Python version and Python paths.

Else you might install a module that is already by default installed in Blender, because pip failed to detect it.  
This can result in clashes and weird bugs.  

## Alternatives
This might (untested) also be achievable by passing `sys.path` to `os.environ["PYTHONPATH"]` and then running one of the below modules.

Existing Python pip wrappers, without handling sys paths by default:
- 100⭐ [di/pip-api](https://github.com/di/pip-api) - local `pip.exe` wrapper, lacks documentation (passes env vars, but not sys path, see [code](https://github.com/di/pip-api/blob/master/pip_api/_call.py))
- 004⭐ [aescarias/pypiwrap](https://github.com/aescarias/pypiwrap) - API wrapper for the PyPI website, not for local `pip.exe` [documentation](https://aescarias.github.io/pypiwrap/)
- 130⭐ [sjkingo/virtualenv-api](https://github.com/sjkingo/virtualenv-api) - local `pip.exe` wrapper, but for virtual env , nice quickstart docs on [README](https://github.com/sjkingo/virtualenv-api/blob/master/README.rst)
- 7k⭐ [pypa/pipx](https://github.com/pypa/pipx) pip wrapper meant for commandline python apps. not really usefull for our use case.

### TODO
- add support for pip auto remove - remove unused dependencies https://github.com/invl/pip-autoremove (does this use it s own uninstall, or can we get a list and use py-pip uninstall)

### used by
- [pip-qt](https://github.com/hannesdelbeke/pip-qt)
- [plugget](https://github.com/plugget/plugget)

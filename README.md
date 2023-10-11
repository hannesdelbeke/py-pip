# pypip
A Python wrapper for `pip.exe` that passes env vars to pip.
Install packages from inside Python.

Features
- pass env vars so pip can detect installed modules in different locations (e.g. Blender dynamicaly changes the Python path on startup)
- use pip from within Python, using the active interpreter

todo
- test pip list with pre installed modules. e.g. nummpy in Blender

similar
- https://github.com/aescarias/pypiwrap
- https://pypi.org/project/pip-api/
- 

used by
- [pip-qt](https://github.com/hannesdelbeke/pip-qt)

# Quick Guide to Making a Python Package

This is a minimal guide for turning your code into a usable package on your local machine or uploadable to PyPi (pip). 
There are many more thorough package-making guides online, such as [this one](https://python-packaging.readthedocs.io/en/latest/index.html). 

## Step 1: Create a package file structure:
Create a directory structure that looks like this (where `mypackage` is the name of your package), and create empty `setup.py` and `__init__.py` files in these locations:
```
mypackage/
    mypackage/
        __init__.py
    setup.py
```

## Step 2: Move your code into the package structure:

Python modules can be placed directly under the `mypackage/mypackage` directory, or in subdirectories in `mypackage/mypackage`:
```
mypackage/
    mypackage/
        myotherfiles/
            myfunctions.py
            myclasses.py
        __init__.py
        mymodule.py
    setup.py
```

## Step 3: Setup the `setup.py` file:
Basically, the `setup.py` file helps direct installation of the package on a machine (similar to a `make` file in other languages).
This file should contain a single call to setuptools.setup(), like so:
```
from setuptools import setup

setup(
      name='mypackage',
      version='0.1',
      description='My awesome package',
      url='http://github.com/mygithub/mypackage',
      author='My Name',
      author_email='myemail@example.com',
      license='MIT',
      packages=['mypackage'], # same as name
      zip_safe=False,
      install_requires=['numpy', 'matplotlib'] # optionally specify dependencies an installer should check for
      )
```

## Step 4: The `__init__.py` file:

Files named `__init__.py` are used to mark directories on disk as Python package directories. When attempting to import a module via `import`, Python will look for modules in directories that are in the Python PATH and that have `__init__.py` files in them. If you remove the `__init__.py` file, Python will no longer look for modules inside that directory, so attempts to import the module will fail.


Often the `__init__.py` contains convenience imports for other modules within your package:

`__init__.py`:
```
import mymodule
import myotherfiles.myfunctions
```

The `__init__.py` file is usually otherwise empty, but Python code (e.g., functions, classes) can be placed directly in this file (not great practice).

### `import` statements in `__init__.py`:

Imports can be handled at least a couple of ways in `__init__.py` (which affect the namespace under which package functions/classes are accessible). Suppose you have the package structure/files from Step 2. 

#### Option 1: Not using `import` in `__init__.py`
```
# __init__.py
# blank
```
```
# some other python code...
>>>import mypackage.myfunctions
>>>mypackage.myfunctions.foo()
"Hello world."
```

#### Option 2: Simple convenience `import` in `__init__.py`
```
# __init__.py
import myfunctions # imports everything in myfunctions.py
```
```
# some other python code...
>>>import mypackage #<- simpler import statement in other code
>>>mypackage.myfunctions.foo()
"Hello world."
```

#### Option 3: Importing functions/classes explicitly in `__init__.py`
```
# __init__.py
from myfunctions import foo # imports only the foo function
#alternative: from myfunctions import * # imports everything in myfunctions.py
```
```
# some other python code...
>>>import mypackage #<- simpler import statement in other code
>>>mypackage.foo() #<- simpler function call in other code
"Hello world."
```

## Installing your package on your local machine:
Navigate to the top level directory of your pacakge (e.g., `mypackage/` here) and run:
```
pip install .
```
That should be it!

## Uploading your package to PyPI for download/installation by others:
This is a bit more involved. Here is a [good guide](https://jonemo.github.io/neubertify/2017/09/13/publishing-your-first-pypi-package/) I found.



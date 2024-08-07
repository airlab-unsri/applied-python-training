# Modules & Packages

## Modules

[Modules](https://docs.python.org/3/tutorial/modules.html) allow you to store reusable blocks of code, such as functions, in separate files. They're referenced by using the `import` statement.

```python
# helpers.py
def display(message, is_warning=False):
    if is_warning:
        print('Warning!!')
    print(message)
```

```python
# import module as namespace
import helpers
helpers.display('Not a warning')

# import all into current namespace
from helpers import *
display('Not a warning')

# import specific items into current namespace
from helpers import display
display('Not a warning')
```

## Packages

[Distribution packages](https://packaging.python.org/glossary/#term-distribution-package) are external archive files which contain resources such as classes and functions. Most every application you create will make use of one or more packages. Imports from packages follow the same syntax as modules you've created. The [Python Package index](https://pypi.org/) contains a full list of packages you can install using [pip](https://pip.pypa.io/en/stable/) or [Poetry](../../getting_started/setup_python/setup_poetry.md).

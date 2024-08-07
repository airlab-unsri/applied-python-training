# Setup pipx

pipx adalah tool yang memungkinkan kamu menginstal dan menjalankan aplikasi Python dalam environment virtual yang terisolasi. Dengan pipx, kamu dapat menginstal aplikasi Python seperti `black`, `flake8`, `isort`, dan `cookiecutter` tanpa khawatir konflik dependensi dengan aplikasi Python lainnya.

Untuk menginstal pipx, jalankan perintah berikut:

`````{tab-set}
````{tab-item} Windows
## Instalasi pipx di Windows

Install menggunakan pip (membutuhkan pip 19.0 atau terbaru)

```{code-block} bash
pip install --user pipx
```

It is possible (even most likely) the above finishes with a WARNING looking similar to this:

Ada kemungkinan instalasi akan berakhir dengan WARNING seperti ini:

```{code-block} bash
WARNING: The script pipx.exe is installed in `<USER folder>\AppData\Roaming\Python\Python3x\Scripts` which is not on PATH
```

Jika iya, buka folder yang disebutkan, sehingga kamu bisa menjalankan executable pipx secara langsung. Masukkan baris berikut (meskipun kamu tidak mendapatkan warning):

```{code-block} bash
.\pipx.exe ensurepath
```

Perintah di atas akan menambahkan path yang disebutkan di atas dan `%USERPROFILE%\.local\bin` ke PATH. Restart terminal kamu dan verifikasi apakah `pipx` berjalan.
````

````{tab-item} Linux
## Instalasi pipx di Linux

* Ubuntu 23.04 atau yang terbaru

```{code-block} bash
sudo apt update
sudo apt install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```
````

````{tab-item} macOS
## Instalasi pipx di macOS

```{code-block} bash
brew install pipx
pipx ensurepath
sudo pipx ensurepath --global # optional to allow pipx actions with --global argument
```
````
`````

## pipx Cheat Sheet

### `pipx install`

```{code-block} bash
pipx install pycowsay
pipx install --python python3.10 pycowsay
pipx install --python 3.12 pycowsay
pipx install --fetch-missing-python --python 3.12 pycowsay
pipx install git+https://github.com/psf/black
pipx install git+https://github.com/psf/black.git@branch-name
pipx install git+https://github.com/psf/black.git@git-hash
pipx install git+ssh://<username>@<private-repo-domain>/<path-to-package.git>
pipx install https://github.com/psf/black/archive/18.9b0.zip
pipx install black[d]
pipx install --preinstall ansible-lint --preinstall mitogen ansible-core
pipx install 'black[d] @ git+https://github.com/psf/black.git@branch-name'
pipx install --suffix @branch-name 'black[d] @ git+https://github.com/psf/black.git@branch-name'
pipx install --include-deps jupyter
pipx install --pip-args='--pre' poetry
pipx install --pip-args='--index-url=<private-repo-host>:<private-repo-port> --trusted-host=<private-repo-host>:<private-repo-port>' private-repo-package
pipx install --index-url https://test.pypi.org/simple/ --pip-args='--extra-index-url https://pypi.org/simple/' some-package
pipx --global install pycowsay
pipx install .
pipx install path/to/some-project
```

### `pipx run`

pipx enables you to test various combinations of Python versions and package versions in ephemeral environments:

```{code-block} bash
pipx run BINARY  # latest version of binary is run with python3
pipx run --spec PACKAGE==2.0.0 BINARY  # specific version of package is run
pipx run --python python3.10 BINARY  # Installed and invoked with specific Python version
pipx run --python python3.9 --spec PACKAGE=1.7.3 BINARY
pipx run --spec git+https://url.git BINARY  # latest version on default branch is run
pipx run --spec git+https://url.git@branch BINARY
pipx run --spec git+https://url.git@hash BINARY
pipx run pycowsay moo
pipx --version  # prints pipx version
pipx run pycowsay --version  # prints pycowsay version
pipx run --python pythonX pycowsay
pipx run pycowsay==2.0 --version
pipx run pycowsay[dev] --version
pipx run --spec git+https://github.com/psf/black.git black
pipx run --spec git+https://github.com/psf/black.git@branch-name black
pipx run --spec git+https://github.com/psf/black.git@git-hash black
pipx run --spec https://github.com/psf/black/archive/18.9b0.zip black --help
pipx run https://gist.githubusercontent.com/cs01/fa721a17a326e551ede048c5088f9e0f/raw/6bdfbb6e9c1132b1c38fdd2f195d4a24c540c324/pipx-demo.py
```

You can run local files, or scripts hosted on the internet, and you can run them with arguments:

```{code-block} bash
pipx run test.py
pipx run test.py 1 2 3
pipx run https://example.com/test.py
pipx run https://example.com/test.py 1 2 3
```

A simple filename is ambiguous - it could be a file, or a package on PyPI. It will be treated as a filename if the file
exists, or as a package if not. To force interpretation as a local path, use `--path`, and to force interpretation as a
package name, use `--spec` (with the PyPI name of the package).

```{code-block} bash
pipx run myscript.py # Local file, if myscript.py exists
pipx run doesnotexist.py # Package, because doesnotexist.py is not a local file
pipx run --path test.py # Always a local file
pipx run --spec test-py test.py # Always a package on PyPI
```

You can also run scripts that have dependencies:

If you have a script `test.py` that needs 3rd party libraries, you can add [inline script metadata](https://packaging.python.org/en/latest/specifications/inline-script-metadata/) in the style of PEP 723.

```{code-block} bash
# test.py

# /// script
# dependencies = ["requests"]
# ///

import sys
import requests
project = sys.argv[1]
pipx_data = requests.get(f"https://pypi.org/pypi/{project}/json").json()
print(pipx_data["info"]["version"])
```

Then you can run it as follows:

```{code-block} bash
> pipx run test.py pipx
1.1.0
```

### `pipx inject`

One use of the inject command is setting up a REPL with some useful extra packages.

```{code-block} bash
> pipx install ptpython
> pipx inject ptpython requests pendulum
```

After running the above commands, you will be able to import and use the `requests` and `pendulum` packages inside a
`ptpython` repl.

Equivalently, the extra packages can be listed in a text file (e.g. `useful-packages.txt`).
Each line is a separate package specifier with the same syntax as the command line.
Comments are supported with a `#` prefix.
Hence, the syntax is a strict subset of the pip [requirements file format][pip-requirements] syntax.

[pip-requirements]: https://pip.pypa.io/en/stable/reference/requirements-file-format/

```{code-block} bash
# Additional packages
requests

pendulum # for easier datetimes
```

This file can then be given to `pipx inject` on the command line:

```{code-block} bash
> pipx inject ptpython --requirement useful-packages.txt
# or:
> pipx inject ptpython -r useful-packages.txt
```

Note that these options can be repeated and used together, e.g.

```{code-block} bash
> pipx inject ptpython package-1 -r extra-packages-1.txt -r extra-packages-2.txt package-2
```

If you require full pip functionality, then use the `runpip` command instead;
however, the installed packages won't be recognised as "injected".

### `pipx list`

```{code-block} bash
> pipx list
venvs are in /Users/user/.local/pipx/venvs
binaries are exposed on your $PATH at /Users/user/.local/bin
   package black 18.9b0, Python 3.10.0
    - black
    - blackd
   package pipx 0.10.0, Python 3.10.0
    - pipx

> pipx list --short
black 18.9b0
pipx 0.10.0
```

### `pipx install-all`

```{code-block} bash
> pipx list --json > pipx.json
> pipx install-all pipx.json
'black' already seems to be installed. Not modifying existing installation in '/usr/local/pipx/venvs/black'. Pass '--force' to force installation.
'pipx' already seems to be installed. Not modifying existing installation in '/usr/local/pipx/venvs/black'. Pass '--force' to force installation.
> pipx install-all pipx.json --force
Installing to existing venv 'black'
  installed package black 24.3.0, installed using Python 3.10.12
  These apps are now globally available
    - black
    - blackd
done! ✨ 🌟 ✨
Installing to existing venv 'pipx'
  installed package pipx 1.4.3, installed using Python 3.10.12
  These apps are now globally available
    - pipx
done! ✨ 🌟 ✨
```

### `pipx upgrade-shared`

One use of the upgrade-shared command is to force a `pip` upgrade.

```{code-block} bash
> pipx upgrade-shared
```

This example pins `pip` (temporarily, until the next automatic upgrade, if that is not explicitly turned off) to a specific version.

```{code-block} bash
> pipx upgrade-shared --pip-args=pip==24.0
```

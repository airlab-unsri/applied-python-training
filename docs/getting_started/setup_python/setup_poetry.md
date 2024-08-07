# Setup Poetry

Poetry adalah tool manajemen dependensi dan package Python yang memungkinkan kamu memanajemen dependensi dalam file `pyproject.toml` dan menginstalnya dengan satu perintah. Poetry juga memungkinkan kamu membuat proyek Python baru dengan struktur direktori yang disarankan.

## Instalasi Poetry

Untuk menginstal Poetry, kamu memerlukan [`pipx`](./setup_pipx).

```{code-block} bash
pipx install poetry
```

Untuk mengupdate Poetry ke versi terbaru, jalankan perintah berikut:

```{code-block} bash
pipx upgrade poetry
```

Untuk menguninstall Poetry:

```{code-block} bash
pipx uninstall poetry
```

## Poetry Cheat Sheet

| Command                           | Description                                                |
| --------------------------------- | ---------------------------------------------------------- |
| `poetry new [name]`               | Creates a new Python project in a new directory.           |
| `poetry init`                     | Initializes a new Poetry project in the current directory. |
| `poetry add [package]`            | Adds a new package to the project's dependencies.          |
| `poetry remove [package]`         | Removes a package from the project's dependencies.         |
| `poetry show`                     | Shows information about the project's packages.            |
| `poetry update`                   | Updates the project's dependencies.                        |
| `poetry install`                  | Installs the project's dependencies.                       |
| `poetry run [command]`            | Runs a command in the virtual environment.                 |
| `poetry shell`                    | Spawns a shell within the virtual environment.             |
| `poetry build`                    | Builds the project package.                                |
| `poetry publish`                  | Publishes the project package to PyPI.                     |
| `poetry version [version]`        | Bumps the version of the project.                          |
| `poetry config [setting] [value]` | Configures Poetry settings.                                |
| `poetry cache clear --all pypi`   | Clears Poetry's cache.                                     |

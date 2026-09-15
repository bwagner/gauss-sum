# Python with uv - translating tutorials

Almost every Python book, website and video uses the commands `python` and
`pip`. We use [`uv`](https://docs.astral.sh/uv/) instead. It does the same jobs,
but it also installs Python for you and has a few more advantages we will get to
later.

The good news: nearly every command you see in a tutorial has a direct uv
equivalent. This guide shows you which one to type.

## Installing uv (once per computer)

You only do this once, and you need an internet connection for it. You do
**not** need to install Python first - uv downloads it for you.

### 1. Open a terminal

- **Windows:** press the Windows key, type `Terminal`, press Enter. (On older
  Windows, type `PowerShell` instead.)
- **macOS:** press `Cmd+Space`, type `Terminal`, press Enter.
- **Linux:** open your terminal app (on Ubuntu: `Ctrl+Alt+T`).

### 2. Run the installer

**Windows:**

```
winget install --id=astral-sh.uv -e
```

If Windows answers that `winget` is not recognized, use this instead:

```
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**

```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 3. Close the terminal and open a new one

The installer tells your computer where to find `uv`, but terminals that are
already open do not notice. A new terminal does.

### 4. Check that it worked

```
uv --version
```

This should print something like `uv 0.9.26`. Then try:

```
uv run python --version
```

The first time, uv downloads Python, so this also needs internet and takes a
moment. After that it is instant.

## The one rule to remember

> **Put `uv run` in front of it.**

If a tutorial says `python something`, you type `uv run something` or
`uv run python something`. That rule covers most of what you will meet.

The tables below all work the same way. **Tutorial says** is the command as you
will find it in a book, website or video. **You type** is what you type instead.

## Running code

| Tutorial says                  | You type                           |
| ------------------------------ | ---------------------------------- |
| `python hello.py`              | `uv run hello.py`                  |
| `python3 hello.py`             | `uv run hello.py`                  |
| `py hello.py` (Windows)        | `uv run hello.py`                  |
| `python` (the `>>>` prompt)    | `uv run python`                    |
| `python -m some_module`        | `uv run python -m some_module`     |
| `python --version`             | `uv run python --version`          |

To leave the `>>>` prompt, type `exit()`.

## Installing packages

A package is code someone else wrote that you can use, like `requests` (for
websites) or `pygame` (for games).

| Tutorial says                          | You type                                |
| -------------------------------------- | --------------------------------------- |
| `pip install requests`                 | `uv add requests`                       |
| `pip uninstall requests`               | `uv remove requests`                    |
| `pip install -r requirements.txt`      | `uv add -r requirements.txt`            |
| `pip install --upgrade requests`       | `uv lock --upgrade-package requests`    |
| `pip list` / `pip freeze`              | `uv tree`                               |

**Never type `pip install` in our projects.** It either installs the package
somewhere your project cannot see, or fails with `No module named pip`. `uv add`
is always the right one.

`uv add` installs the package and writes its name into a file named
`pyproject.toml`, so next time, and on any other computer, `uv run` knows what
your project needs.

## Virtual environments

Tutorials often tell you to do this first:

```
python -m venv .venv
.venv\Scripts\activate          (Windows)
source .venv/bin/activate       (macOS / Linux)
```

**Skip all of it.** uv creates the `.venv` folder by itself the first time you
run `uv run` or `uv add`, and there is nothing to activate. When a tutorial says
"make sure your virtual environment is active", `uv run` already takes care of
that.

## Starting a new project

Tutorials usually say "make a folder and create a file". With uv:

```
uv init my_game
cd my_game
uv run main.py
```

`uv init` creates the folder with a few files already inside:

- `main.py` - a small starting program you can change
- `pyproject.toml` - the project's settings and the list of packages it uses
- `.python-version` - which Python version this project uses
- `README.md` - a description of the project, for you to fill in
- `.gitignore` and a Git repository, for saving versions of your work

## One file with its own packages

Sometimes you only want a single script, not a whole project. uv can write the
package list into the top of the file itself:

```
uv init --script weather.py
uv add --script weather.py requests
uv run weather.py
```

Open `weather.py` and you will see a `# /// script` block at the top. That block
is the package list. You can send this one file to a friend with uv, and
`uv run weather.py` works for them too.

## Different Python versions

| Tutorial says                  | You type                              |
| ------------------------------ | ------------------------------------- |
| "Install Python 3.12 first"    | nothing - uv downloads it when needed |
| `py -3.12 hello.py` (Windows)  | `uv run --python 3.12 hello.py`       |
| "Which Pythons do I have?"     | `uv python list`                      |

## Programs that come as packages

Some packages are not for importing but are programs you run, like `ruff`
(checks your code) or `pycowsay` (a cow that talks).

| Tutorial says                          | You type                        |
| -------------------------------------- | ------------------------------- |
| `pip install pycowsay` then `pycowsay` | `uvx pycowsay hello`            |
| `pipx run pycowsay hello`              | `uvx pycowsay hello`            |
| `pipx install ruff`                    | `uv tool install ruff`          |

`uvx` runs the program once without installing it for good.

## Jupyter notebooks

| Tutorial says                          | You type                                  |
| -------------------------------------- | ----------------------------------------- |
| `pip install jupyter` then `jupyter lab` | `uv run --with jupyter jupyter lab`     |

## Files you will see in a uv project

| File or folder     | What it is                                 | Should you edit it?          |
| ------------------ | ------------------------------------------ | ---------------------------- |
| `pyproject.toml`   | project settings and package list          | yes, but `uv add` is easier  |
| `uv.lock`          | exact versions of every package            | no, uv writes it             |
| `.venv/`           | the installed Python and packages          | no - and it is safe to delete |
| `.python-version`  | the Python version for this project        | rarely                       |

## Your editor

If you use **VS Code**, it has to know about the project's `.venv` folder,
otherwise the Run button uses a different Python and cannot find your packages.

1. Run `uv run` once in the project so `.venv` exists.
2. In VS Code press `Ctrl+Shift+P`, type **Python: Select Interpreter**.
3. Pick the one that mentions `.venv`.

## When something goes wrong

| What you see                                              | What happened and what to do                                                                                   |
| --------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Typing `python` opens the Microsoft Store                 | You forgot `uv run`. Type `uv run python`.                                                                     |
| `No module named pip`                                     | You used `pip install`. Use `uv add` instead.                                                                  |
| `ModuleNotFoundError: No module named 'requests'`         | Run `uv add requests`. If you already did, you probably ran the file without `uv run`, or VS Code uses the wrong Python (see above). |
| `uv: command not found` / `uv is not recognized`          | Close the terminal and open a new one. If it still happens, uv is not installed yet - see *Installing uv* at the top.                           |
| Something is strange and nothing helps                    | Delete the `.venv` folder and type `uv run` again. uv builds it fresh from `pyproject.toml`.                   |

## Keeping uv up to date

- Installed with winget: `winget upgrade --id=astral-sh.uv`
- Installed with the `powershell ...` or `curl ...` command: `uv self update`

## Learning more

- uv documentation: https://docs.astral.sh/uv/
- `uv help` lists every command, and `uv help add` explains one of them.

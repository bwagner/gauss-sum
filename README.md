# mathe

Gauss summation formula - `gauss.py` plus tests.

New to uv, or following a Python tutorial that uses `python` and `pip`? See
[python-with-uv.md](python-with-uv.md) for the uv equivalent of each command.

## Setup

You only need one tool: [uv](https://docs.astral.sh/uv/). It installs Python for
you and manages the virtual environment, so there is nothing else to install
first.

To install uv, follow
[Installing uv](python-with-uv.md#installing-uv-once-per-computer) in the guide.

## Running

There is no activation step and no `pip install`. The first command you run
downloads a matching Python, creates `.venv`, and installs the dependencies
listed in `pyproject.toml`:

```
uv run gauss.py 10          # sum 1..10
uv run gauss.py 5 10        # sum 5..10
uv run gauss.py --help      # usage
```

## Tests

```
uv run pytest
```

## Notes

These commands are identical on Windows, macOS and Linux.

Write `uv run gauss.py` rather than `./gauss.py`. The shebang at the top of the
script is honored on macOS and Linux only; Windows has no shebang support at the
OS level, so `./gauss.py` there depends on a separate python.org installation
and would not use this project's virtual environment.
 
# gauss-sum

A worked example that starts with the formula young Gauss is said to have found
for 1 + 2 + ... + 100 and turns it into a small, tested Python program.

The formula `n(n+1)/2` adds up 1..n without a loop. `gauss.py` builds on it to
sum any range, including negative numbers, and to sum only the even or only the
odd numbers. `test_gauss.py` tests each of these, and the command line too.

The project uses [uv](https://docs.astral.sh/uv/) rather than `python` and
`pip`. Most Python tutorials use the latter, so
[python-with-uv.md](python-with-uv.md) shows the uv command for each one you
will meet.

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
 
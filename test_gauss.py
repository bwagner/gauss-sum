import subprocess
import sys
from pathlib import Path

import pytest

import gauss

GAUSS = Path(__file__).parent / "gauss.py"


def test_sum_1_to_n():
    assert 55 == gauss.sum_1_to_n(10)


@pytest.mark.parametrize("n, expected", [(-1, 0), (-2, 1), (-4, 6), (-5, 10)])
def test_sum_1_to_n_accepts_negative_n(n, expected):
    assert expected == gauss.sum_1_to_n(n)


@pytest.mark.parametrize("n", [0, 1, 3, 10, 99])
def test_sum_1_to_n_mirrors_around_minus_one_half(n):
    """f(n) == f(-n-1); this symmetry is what lets sum_range span zero."""
    assert gauss.sum_1_to_n(n) == gauss.sum_1_to_n(-n - 1)


def test_sum_range_5_to_10():
    assert 45 == gauss.sum_range(5, 10)


@pytest.mark.parametrize(
    "lower, upper", [(-3, 3), (-10, -5), (-1, 1), (-1, 0), (0, 5), (-7, 2)]
)
def test_sum_range_spans_negative_bounds(lower, upper):
    assert sum(range(lower, upper + 1)) == gauss.sum_range(lower, upper)


def test_sum_range_single_value():
    assert 7 == gauss.sum_range(7, 7)


def test_sum_range_from_1_matches_sum_1_to_n():
    assert gauss.sum_1_to_n(10) == gauss.sum_range(1, 10)


def test_sum_range_returns_int():
    assert isinstance(gauss.sum_range(5, 10), int)


def test_sum_even_1_to_n():
    assert 30 == gauss.sum_even_1_to_n(10)


def test_sum_even_handles_odd_n():
    assert 12 == gauss.sum_even_1_to_n(7)


def test_sum_odd_1_to_n():
    assert 25 == gauss.sum_odd_1_to_n(9)


def test_sum_odd_handles_even_n():
    assert 25 == gauss.sum_odd_1_to_n(10)


@pytest.mark.parametrize("n", [1, 2, 7, 10, 99, 100])
def test_even_plus_odd_equals_total(n):
    assert gauss.sum_1_to_n(n) == gauss.sum_even_1_to_n(n) + gauss.sum_odd_1_to_n(n)


def test_even_and_odd_return_int():
    assert isinstance(gauss.sum_even_1_to_n(10), int)
    assert isinstance(gauss.sum_odd_1_to_n(10), int)


@pytest.mark.parametrize("bad_n", [-1, -5])
def test_sum_even_rejects_negative_n(bad_n):
    with pytest.raises(ValueError):
        gauss.sum_even_1_to_n(bad_n)


@pytest.mark.parametrize("bad_n", [-1, -5])
def test_sum_odd_rejects_negative_n(bad_n):
    with pytest.raises(ValueError):
        gauss.sum_odd_1_to_n(bad_n)


def test_sum_even_and_odd_accept_zero():
    assert 0 == gauss.sum_even_1_to_n(0)
    assert 0 == gauss.sum_odd_1_to_n(0)


def test_sum_range_rejects_reversed_bounds():
    with pytest.raises(ValueError):
        gauss.sum_range(10, 5)


def test_cli_single_argument(capsys):
    assert 0 == gauss.main(["10"])
    assert "Sum is 55" == capsys.readouterr().out.strip()


def test_cli_range(capsys):
    assert 0 == gauss.main(["5", "10"])
    assert "Sum is 45" == capsys.readouterr().out.strip()


def test_cli_reversed_bounds_reports_error(capsys):
    assert 1 == gauss.main(["10", "5"])
    captured = capsys.readouterr()
    assert "" == captured.out.strip()
    assert "10 is greater than 5" in captured.err


def test_cli_rejects_non_integer(capsys):
    with pytest.raises(SystemExit) as exit_info:
        gauss.main(["ab"])
    assert 2 == exit_info.value.code
    captured = capsys.readouterr()
    assert "usage:" in captured.err
    assert "ab" in captured.err


def test_cli_requires_an_argument(capsys):
    with pytest.raises(SystemExit) as exit_info:
        gauss.main([])
    assert 2 == exit_info.value.code
    assert "required: upper" in capsys.readouterr().err.lower()


def test_cli_rejects_extra_arguments(capsys):
    with pytest.raises(SystemExit) as exit_info:
        gauss.main(["1", "2", "3"])
    assert 2 == exit_info.value.code
    assert "usage:" in capsys.readouterr().err


def test_cli_help(capsys):
    with pytest.raises(SystemExit) as exit_info:
        gauss.main(["--help"])
    assert 0 == exit_info.value.code
    captured = capsys.readouterr()
    assert "usage:" in captured.out
    assert "[LOWER] UPPER" in captured.out


def test_script_runs_as_a_process():
    result = subprocess.run(
        [sys.executable, str(GAUSS), "10"],
        capture_output=True,
        text=True,
        check=False,
    )
    assert 0 == result.returncode
    assert "Sum is 55" == result.stdout.strip()

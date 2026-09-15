import argparse
import sys


def sum_range(lower, upper):
    if lower > upper:
        raise ValueError(f"{lower} is greater than {upper}")
    return sum_1_to_n(upper) - sum_1_to_n(lower - 1)


def sum_1_to_n(n):
    return n * (n + 1) // 2


def sum_even_1_to_n(n):
    if n < 0:
        raise ValueError(f"{n} is negative")
    even_count = n // 2
    return even_count * (even_count + 1)


def sum_odd_1_to_n(n):
    if n < 0:
        raise ValueError(f"{n} is negative")
    odd_count = (n + 1) // 2
    return odd_count**2


def parse_args(argv=None):
    parser = argparse.ArgumentParser(
        description="Sum consecutive integers using the Gauss summation formula."
    )
    parser.add_argument(
        "lower",
        type=int,
        nargs="?",
        default=1,
        metavar="LOWER",
        help="lower bound (default: 1)",
    )
    parser.add_argument("upper", type=int, metavar="UPPER", help="upper bound")
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    try:
        total = sum_range(args.lower, args.upper)
    except ValueError as error:
        print(f"Sum is undefined: {error}", file=sys.stderr)
        return 1
    print(f"Sum is {total}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

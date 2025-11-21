"""Day 6: Custom Customs"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from collections import Counter
from itertools import groupby


def main():
    """Solve day 6 puzzles."""
    with open("inputs/day_6.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return sum(len(set("".join(group))) for group in get_groups(puzzle_input))


def star_2(puzzle_input):
    """Solve second puzzle."""
    return sum(
        sum(count == len(group) for count in Counter("".join(group)).values())
        for group in get_groups(puzzle_input)
    )


def get_groups(puzzle_input):
    """Get the groups of people."""
    return tuple(
        tuple(group) for key, group in groupby(puzzle_input, key=bool) if key
    )


if __name__ == "__main__":
    main()

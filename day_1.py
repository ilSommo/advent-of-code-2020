"""Day 1: Report Repair"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from itertools import combinations
from math import prod


def main():
    """Solve day 1 puzzles."""
    with open("inputs/day_1.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    entries = parse_input(puzzle_input)

    for entries_combination in combinations(entries, 2):
        if sum(entries_combination) == 2020:
            return prod(entries_combination)

    return None


def star_2(puzzle_input):
    """Solve second puzzle."""
    entries = parse_input(puzzle_input)

    for entries_combination in combinations(entries, 3):
        if sum(entries_combination) == 2020:
            return prod(entries_combination)

    return None


def parse_input(puzzle_input):
    """Parse puzzle input."""
    return tuple(int(line) for line in puzzle_input)


if __name__ == "__main__":
    main()

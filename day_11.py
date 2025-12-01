"""Day 11: Seating System"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from functools import cache
from itertools import product


def main():
    """Solve day 11 puzzles."""
    with open("inputs/day_11.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    empty, occupied = parse_input(puzzle_input)

    while True:
        new_empty = set()
        new_occupied = set()

        for seat in empty:
            if len(compute_adjacent(seat) & occupied) == 0:
                new_occupied.add(seat)
            else:
                new_empty.add(seat)

        for seat in occupied:
            if len(compute_adjacent(seat) & occupied) >= 4:
                new_empty.add(seat)
            else:
                new_occupied.add(seat)

        if new_empty == empty:
            return len(new_occupied)

        empty, occupied = new_empty, new_occupied


def star_2(puzzle_input):
    """Solve second puzzle."""
    empty, occupied = parse_input(puzzle_input)
    seats = frozenset(empty | occupied)

    while True:
        new_empty = set()
        new_occupied = set()

        for seat in empty:
            if len(compute_visible(seat, seats) & occupied) == 0:
                new_occupied.add(seat)
            else:
                new_empty.add(seat)

        for seat in occupied:
            if len(compute_visible(seat, seats) & occupied) >= 5:
                new_empty.add(seat)
            else:
                new_occupied.add(seat)

        if new_empty == empty:
            return len(new_occupied)

        empty, occupied = new_empty, new_occupied


@cache
def compute_adjacent(seat):
    """Compute adjacent coordinates to a seat."""
    return frozenset(
        set(seat + ii + jj * 1j for ii, jj in product((-1, 0, +1), repeat=2))
        - {seat}
    )


@cache
def compute_visible(seat, seats):
    """Compute first visible seat in all directions."""
    max_i = max(s.real for s in seats)
    max_j = max(s.imag for s in seats)

    visible = set()

    for ii, jj in product((-1, 0, +1), repeat=2):
        direction = ii + jj * 1j

        if direction == 0:
            continue

        position = seat + direction

        while 0 <= position.real <= max_i and 0 <= position.imag <= max_j:
            if position in seats:
                visible.add(position)
                break

            position += direction

    return frozenset(visible)


def parse_input(puzzle_input):
    """Convert puzzle input into sets of coordinates."""
    empty = set()
    occupied = set()

    for i, line in enumerate(puzzle_input):
        for j, char in enumerate(line):
            if char == "L":
                empty.add(i + j * 1j)
            elif char == "#":
                occupied.add(i + j * 1j)

    return empty, occupied


if __name__ == "__main__":
    main()

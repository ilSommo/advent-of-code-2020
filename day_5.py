"""Day 5: Binary Boarding"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 5 puzzles."""
    with open("inputs/day_5.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return max(compute_id(seat) for seat in puzzle_input)


def star_2(puzzle_input):
    """Solve second puzzle."""
    ids = sorted(compute_id(seat) for seat in puzzle_input)

    for i, seat_id in enumerate(ids[:-1]):
        if ids[i + 1] != seat_id + 1:
            return seat_id + 1

    return None


def compute_id(seat):
    """Compute the ID for a seat"""
    row = sum(2 ** (6 - i) * (char == "B") for i, char in enumerate(seat[:7]))
    col = sum(2 ** (2 - i) * (char == "R") for i, char in enumerate(seat[7:]))

    return row * 8 + col


if __name__ == "__main__":
    main()

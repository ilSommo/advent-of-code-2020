"""Day 3: Toboggan Trajectory"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 3 puzzles."""
    with open("inputs/day_3.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file.readlines())

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    return get_trees(puzzle_input, 3, 1)


def star_2(puzzle_input):
    """Solve second puzzle."""
    return (
        get_trees(puzzle_input, 1, 1)
        * get_trees(puzzle_input, 3, 1)
        * get_trees(puzzle_input, 5, 1)
        * get_trees(puzzle_input, 7, 1)
        * get_trees(puzzle_input, 1, 2)
    )


def get_trees(puzzle_input, right, down):
    """Get tree coordinates from puzzle input."""
    period = len(puzzle_input[0])

    return sum(
        line[right * i % period] == "#"
        for i, line in enumerate(puzzle_input[::down])
    )


if __name__ == "__main__":
    main()

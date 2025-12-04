"""Day 15: Rambunctious Recitation"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 15 puzzles."""
    with open("inputs/day_15.txt", encoding="ascii") as input_file:
        puzzle_input = input_file.read().rstrip()

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    numbers = get_starting_numbers(puzzle_input)

    return compute_turn(numbers, 2020)


def star_2(puzzle_input):
    """Solve second puzzle."""
    numbers = get_starting_numbers(puzzle_input)

    return compute_turn(numbers, 30000000)


def compute_turn(numbers, turn):
    """Compute value of number at given turn."""
    last_seen = {number: i for i, number in enumerate(numbers[:-1], start=1)}
    current = numbers[-1]

    for i in range(len(numbers), turn):
        if current in last_seen:
            number = i - last_seen[current]
        else:
            number = 0

        last_seen[current] = i
        current = number

    return current


def get_starting_numbers(puzzle_input):
    """Get starting numbers from input."""
    return tuple(map(int, puzzle_input.split(",")))


if __name__ == "__main__":
    main()

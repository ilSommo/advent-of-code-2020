"""Day 9: Encoding Error"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from itertools import product

PREAMBLE_LENGTH = 25


def main():
    """Solve day 9 puzzles."""
    with open("inputs/day_9.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    numbers = get_numbers(puzzle_input)

    for i in range(PREAMBLE_LENGTH, len(numbers) - PREAMBLE_LENGTH):
        if numbers[i] not in map(
            sum, product(set(numbers[i - PREAMBLE_LENGTH : i]), repeat=2)
        ):
            return numbers[i]

    return None


def star_2(puzzle_input):
    """Solve second puzzle."""
    numbers = get_numbers(puzzle_input)
    number = star_1(puzzle_input)

    i, j = (0, 2)

    while True:
        contiguous_sum = sum(numbers[i:j])

        if contiguous_sum == number:
            break

        if contiguous_sum < number:
            j += 1
        else:
            i += 1

    return min(numbers[i:j]) + max(numbers[i:j])


def get_numbers(puzzle_input):
    """Get number list from input."""
    return tuple(map(int, puzzle_input))


if __name__ == "__main__":
    main()

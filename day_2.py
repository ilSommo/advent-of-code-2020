"""Day 2: Password Philosophy"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 2 puzzles."""
    with open("inputs/day_2.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    valid = 0

    for line in puzzle_input:
        parts = line.split()

        min_times, max_times = map(int, parts[0].split("-"))
        letter = parts[1][0]
        password = parts[2]

        valid += int(min_times <= password.count(letter) <= max_times)

    return valid


def star_2(puzzle_input):
    """Solve second puzzle."""
    valid = 0

    for line in puzzle_input:
        parts = line.split()

        index_0, index_1 = map(int, parts[0].split("-"))
        letter = parts[1][0]
        password = parts[2]

        valid += (password[index_0 - 1] == letter) ^ (
            password[index_1 - 1] == letter
        )

    return valid


if __name__ == "__main__":
    main()

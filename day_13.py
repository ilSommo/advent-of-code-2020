"""Day 13: Shuttle Search"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from math import prod


def main():
    """Solve day 13 puzzles."""
    with open("inputs/day_13.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    earliest, buses = parse_input(puzzle_input)

    times = {
        bus: bus * (earliest // bus + 1) for bus in buses if bus is not None
    }

    bus, time = min(times.items(), key=lambda time: time[1])

    return bus * (time - earliest)


def star_2(puzzle_input):
    """Solve second puzzle."""
    _, buses = parse_input(puzzle_input)
    constraints = []

    for i, bus in enumerate(buses):
        if bus is None:
            continue

        constraints.append((-i % bus, bus))

    N = prod(n_i for _, n_i in constraints)
    x = 0

    for a_i, n_i in constraints:
        N_i = N // n_i
        M_i = 1

        while (N_i * M_i) % n_i != 1:
            M_i += 1

        x += a_i * N_i * M_i

    return x % N


def parse_input(puzzle_input):
    """Parse puzzle input."""
    earliest = int(puzzle_input[0])
    buses = tuple(
        int(bus) if bus != "x" else None for bus in puzzle_input[1].split(",")
    )

    return earliest, buses


if __name__ == "__main__":
    main()

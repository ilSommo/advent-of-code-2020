"""Day 10: Adapter Array"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 10 puzzles."""
    with open("inputs/day_10.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    adapters = get_adapters(puzzle_input)
    differences = []

    for i, adapter in enumerate(adapters[:-1]):
        differences.append(adapters[i + 1] - adapter)

    return differences.count(3) * differences.count(1)


def star_2(puzzle_input):
    """Solve second puzzle."""
    adapters = get_adapters(puzzle_input)
    ways = {0: 1}

    for adapter in adapters[1:]:
        ways[adapter] = (
            ways.get(adapter - 3, 0)
            + ways.get(adapter - 2, 0)
            + ways.get(adapter - 1, 0)
        )

    return ways[adapters[-1]]


def get_adapters(puzzle_input):
    """Get sorted adapters from input."""
    adapters = sorted(list(map(int, puzzle_input)))
    adapters.append(adapters[-1] + 3)

    return tuple([0] + adapters)


if __name__ == "__main__":
    main()

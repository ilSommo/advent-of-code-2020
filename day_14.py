"""Day 14: Docking Data"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from collections import deque


def main():
    """Solve day 14 puzzles."""
    with open("inputs/day_14.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = parse_input(puzzle_input)

    memory = {}
    mask = None

    for address, value in instructions:
        if address == "mask":
            mask = value

        else:
            memory[address] = apply_mask(value, mask)

    return sum(memory.values())


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = parse_input(puzzle_input)

    memory = {}
    mask = None

    for address, value in instructions:
        if address == "mask":
            mask = value

        else:
            addresses = apply_mask_v2(address, mask)

            for address in addresses:
                memory[address] = value

    return sum(memory.values())


def apply_mask(value, mask):
    """Apply mask to a value."""
    binary = format(value, "036b")

    result = "".join(
        bit if mask_bit == "X" else mask_bit
        for bit, mask_bit in zip(binary, mask)
    )

    return int(result, 2)


def apply_mask_v2(address, mask):
    """Return all addresses to overwrite."""
    binary = format(address, "036b")

    masked = "".join(
        bit if mask_bit == "0" else mask_bit
        for bit, mask_bit in zip(binary, mask)
    )

    addresses = []
    floating = deque([masked])

    while floating:
        address = floating.popleft()

        if "X" not in address:
            addresses.append(int("".join(address), 2))
            continue

        floating.extend(
            [address.replace("X", "0", 1), address.replace("X", "1", 1)]
        )

    return tuple(addresses)


def parse_input(puzzle_input):
    """Get mask and instructions from input."""
    instructions = []

    for line in puzzle_input:
        if "mask" in line:
            instructions.append(("mask", line.split()[-1]))

        else:
            address = int(line.split("[")[1].split("]")[0])
            value = int(line.split()[-1])
            instructions.append((address, value))

    return tuple(instructions)


if __name__ == "__main__":
    main()

"""Day 12: Rain Risk"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


def main():
    """Solve day 12 puzzles."""
    with open("inputs/day_12.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    instructions = parse_input(puzzle_input)

    position = 0 + 0j
    direction = 1

    for instruction in instructions:
        position, direction = move_1(position, direction, instruction)

    return int(abs(position.real) + abs(position.imag))


def star_2(puzzle_input):
    """Solve second puzzle."""
    instructions = parse_input(puzzle_input)

    ship = 0 + 0j
    waypoint = 10 + 1j

    for instruction in instructions:
        ship, waypoint = move_2(ship, waypoint, instruction)

    return int(abs(ship.real) + abs(ship.imag))


def move_1(position, direction, instruction):
    """Move ship according to an instruction."""
    action, value = instruction

    match action:
        case "N":
            position += 1j * value
        case "S":
            position -= 1j * value
        case "E":
            position += value
        case "W":
            position -= value
        case "L":
            direction *= 1j ** (value / 90)
        case "R":
            direction /= 1j ** (value / 90)
        case "F":
            position += direction * value

    return position, direction


def move_2(ship, waypoint, instruction):
    """Move ship and waypoint according to an instruction."""
    action, value = instruction

    match action:
        case "N":
            waypoint += 1j * value
        case "S":
            waypoint -= 1j * value
        case "E":
            waypoint += value
        case "W":
            waypoint -= value
        case "L":
            waypoint *= 1j ** (value / 90)
        case "R":
            waypoint /= 1j ** (value / 90)
        case "F":
            ship += waypoint * value

    return ship, waypoint


def parse_input(puzzle_input):
    """Parse puzzle input."""
    return tuple((line[0], int(line[1:])) for line in puzzle_input)


if __name__ == "__main__":
    main()

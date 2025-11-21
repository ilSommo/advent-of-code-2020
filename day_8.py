"""Day 8: Handheld Halting"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"


class Console:
    """Class representing a console."""

    def __init__(self, code):
        """Constructor method."""
        self.acc = 0
        self.i = 0
        self.code = code

    def run(self):
        """Run the whole program."""
        self.i = 0
        executed = set()

        while self.i not in executed and self.i < len(self.code):
            executed.add(self.i)
            self.step()

        return self.i >= len(self.code), self.acc

    def step(self):
        """Execute one step."""
        operation, argument = self.code[self.i]

        match operation:
            case "acc":
                self.acc += argument
            case "jmp":
                self.i += argument - 1

        self.i += 1


def main():
    """Solve day 8 puzzles."""
    with open("inputs/day_8.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    code = get_instructions(puzzle_input)
    console = Console(code)

    return console.run()[1]


def star_2(puzzle_input):
    """Solve second puzzle."""
    code = get_instructions(puzzle_input)

    for i, (operation, argument) in enumerate(code):
        if operation == "acc":
            continue

        new_code = list(code)
        new_code[i] = ("nop" if operation == "jmp" else "jmp", argument)

        console = Console(new_code)
        fixed, acc = console.run()

        if fixed:
            return acc

    return None


def get_instructions(puzzle_input):
    """Get instructions from input."""
    return tuple(
        (operation, int(argument))
        for operation, argument in (line.split() for line in puzzle_input)
    )


if __name__ == "__main__":
    main()

"""Day 16: Ticket Translation"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from math import prod


def main():
    """Solve day 16 puzzles."""
    with open("inputs/day_16.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    rules, _, tickets = parse_note(puzzle_input)

    return sum(
        value
        for ticket in tickets
        for value in ticket
        if not is_valid_value(value, rules)
    )


def star_2(puzzle_input):
    """Solve second puzzle."""
    rules, my_ticket, tickets = parse_note(puzzle_input)
    valid_tickets = [my_ticket] + [
        ticket for ticket in tickets if is_valid_ticket(ticket, rules)
    ]

    fields = [
        tuple(ticket[i] for ticket in valid_tickets)
        for i in range(len(my_ticket))
    ]

    rule_to_index = {
        rule: {
            i for i, field in enumerate(fields) if matches_rule(field, ranges)
        }
        for rule, ranges in rules.items()
    }

    solution = {}

    while rule_to_index:
        rule, indices = min(rule_to_index.items(), key=lambda x: len(x[1]))
        index = indices.pop()
        solution[rule] = index

        del rule_to_index[rule]

        for v in rule_to_index.values():
            v.discard(index)

    return prod(
        my_ticket[v] for k, v in solution.items() if k.startswith("departure")
    )


def is_valid_ticket(ticket, rules):
    """Check if a ticket is valid."""
    return all(is_valid_value(value, rules) for value in ticket)


def is_valid_value(value, rules):
    """Check if a value is valid for any rule."""
    return any(
        start <= value <= end
        for ranges in rules.values()
        for start, end in ranges
    )


def matches_rule(field, ranges):
    """Check if all field values satisfy the given ranges."""
    return all(
        any(start <= value <= end for start, end in ranges) for value in field
    )


def parse_note(puzzle_input):
    """Get rules and tickets."""
    blanks = (
        puzzle_input.index("your ticket:") - 1,
        puzzle_input.index("nearby tickets:") - 1,
    )

    rules = {}

    for line in puzzle_input[: blanks[0]]:
        rule = line.split(":")[0]
        rules[rule] = tuple(
            tuple(map(int, range_.split("-")))
            for range_ in line.split(": ")[1].split(" or ")
        )

    my_ticket = tuple(map(int, puzzle_input[blanks[1] - 1].split(",")))

    tickets = tuple(
        tuple(map(int, line.split(",")))
        for line in puzzle_input[blanks[1] + 2 :]
    )

    return rules, my_ticket, tickets


if __name__ == "__main__":
    main()

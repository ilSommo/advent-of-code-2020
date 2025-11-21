"""Day 7: Handy Haversacks"""

__author__ = "Martino M. L. Pulici <martino.pulici@proton.me>"
__date__ = "2025"
__license__ = "MIT"

from collections import defaultdict, deque


def main():
    """Solve day 7 puzzles."""
    with open("inputs/day_7.txt", encoding="ascii") as input_file:
        puzzle_input = tuple(line.rstrip() for line in input_file)

    print(star_1(puzzle_input))
    print(star_2(puzzle_input))


def star_1(puzzle_input):
    """Solve first puzzle."""
    graph = get_graph(puzzle_input)

    return sum("shiny gold" in values for values in graph.values())


def star_2(puzzle_input):
    """Solve second puzzle."""
    graph = get_graph(puzzle_input)

    return sum(graph["shiny gold"].values())


def expand_graph(graph):
    """Get recursive content."""
    expanded_graph = {}

    for container, contents in graph.items():
        expanded_contents = defaultdict(int)
        contents_queue = deque(contents.items())

        while contents_queue:
            colour, number = contents_queue.popleft()
            expanded_contents[colour] += number
            contents_queue.extend(
                (k, v * number) for k, v in graph[colour].items()
            )

        expanded_graph[container] = dict(expanded_contents)

    return expanded_graph


def get_graph(puzzle_input):
    """Get graph of bags contents."""
    graph = {}

    for line in puzzle_input:
        container, contents = line.split(" bags contain ")
        graph[container] = {}

        if contents == "no other bags.":
            continue

        for content in contents.split(", "):
            parts = content.split()
            graph[container][" ".join(parts[1:-1])] = int(parts[0])

    return expand_graph(graph)


if __name__ == "__main__":
    main()

from itertools import cycle
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 8: Haunted Wasteland", caption="part - 1")
def solution(content: str) -> int:
	totals = 0

	directions, _, *str_ways = content.splitlines()
	ways = {way[0:3]: (way[7:10], way[12:15]) for way in str_ways}

	position = "AAA"
	c = cycle(int(d == "R") for d in directions)

	while not position == "ZZZ":
		totals += 1
		position = ways[position][next(c)]

	return totals


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

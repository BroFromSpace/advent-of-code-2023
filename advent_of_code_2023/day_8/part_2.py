from itertools import cycle
from math import lcm
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 8: Haunted Wasteland", caption="part - 2")
def solution(content: str) -> int:
	directions, _, *str_ways = content.splitlines()
	ways = {way[0:3]: (way[7:10], way[12:15]) for way in str_ways}

	positions = [way for way in ways if way.endswith("A")]
	totals = [0] * len(positions)

	for i, pos in enumerate(positions):
		c = cycle(int(d == "R") for d in directions)

		while not pos.endswith("Z"):
			totals[i] += 1
			pos = ways[pos][next(c)]

	return lcm(*totals)


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

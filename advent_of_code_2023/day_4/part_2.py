from collections import defaultdict
from pathlib import Path
from typing import DefaultDict

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


@pretty_output(title="Day 4: Scratchcards - Part 2", caption="part - 2")
def solution(lines: list[str]) -> int:
	total_points = 0
	scratchcard_points: DefaultDict[int, int] = defaultdict(int)

	for i, line in enumerate(lines):
		scratchcard_points[i] += 1
		winning_numbers, my_numbers = line.split("|")

		winning_set = set(winning_numbers.split())
		my_set = set(my_numbers.split())

		for j in range(len(winning_set.intersection(my_set))):
			scratchcard_points[i + j + 1] += scratchcard_points[i]

		total_points += scratchcard_points[i]

	return total_points


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

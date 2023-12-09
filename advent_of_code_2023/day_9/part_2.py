from itertools import pairwise
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


def extrapolate(sequence: list[int]) -> int:
	if all(x == 0 for x in sequence):
		return 0

	deltas = [b - a for a, b in pairwise(sequence)]
	return sequence[0] - extrapolate(deltas)


@pretty_output(title="Day 9: Mirage Maintenance", caption="part - 2")
def solution(lines: list[str]) -> int:
	total = 0

	for line in lines:
		total += extrapolate(list(map(int, line.split())))

	return total


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

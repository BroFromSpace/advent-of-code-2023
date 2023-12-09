from itertools import pairwise
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


def extrapolate(sequence: list[int]) -> int:
	if all(x == 0 for x in sequence):
		return 0

	deltas = [b - a for a, b in pairwise(sequence)]
	return sequence[-1] + extrapolate(deltas)


@pretty_output(title="Day 9: Mirage Maintenance", caption="part - 1")
def solution(lines: list[str]) -> int:
	result = 0

	for line in lines:
		result += extrapolate(list(map(int, line.split())))

	return result


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

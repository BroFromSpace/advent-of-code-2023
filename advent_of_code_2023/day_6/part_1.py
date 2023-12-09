import math
import re
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 6: Wait For It", caption="part - 1")
def solution(lines: str) -> int:
	total = 1
	times_str, distances_str = lines.splitlines()

	times = map(int, re.findall(r"\d+", times_str))
	distances = map(int, re.findall(r"\d+", distances_str))

	for t, d in zip(times, distances):
		# (t - x) * x = d
		# -(t^2) + tx - d = 0

		discriminant = t**2 - 4 * d
		x1 = (-t - math.sqrt(discriminant)) / -2
		x2 = (-t + math.sqrt(discriminant)) / -2

		range_start = math.floor(min(x1, x2) + 1)
		range_end = math.ceil(max(x1, x2) - 1)

		total *= abs(range_end - range_start) + 1

	return total


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

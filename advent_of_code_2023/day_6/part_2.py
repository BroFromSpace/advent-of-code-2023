import math
import re
from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 6: Wait For It", caption="part - 2")
def solution(lines: str) -> int:
	times, distances = lines.splitlines()

	time = int(re.sub(r"\D", "", times))
	distance = int(re.sub(r"\D", "", distances))

	discriminant = time**2 - 4 * distance
	x1 = (-time - math.sqrt(discriminant)) / -2
	x2 = (-time + math.sqrt(discriminant)) / -2

	range_start = math.floor(min(x1, x2) + 1)
	range_end = math.ceil(max(x1, x2) - 1)

	return abs(range_end - range_start) + 1


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

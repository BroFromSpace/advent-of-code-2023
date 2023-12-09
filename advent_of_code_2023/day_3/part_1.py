from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

SYMBOLS = {"/", "+", "#", "$", "-", "&", "%", "=", "@", "*"}


@pretty_output(title="Day 3: Gear Ratios - Part 1", caption="part - 1")
def solution(lines: list[str]):
	schema_height = len(lines) - 1
	schema_length = len(lines[0]) - 1

	def _get_nearest_symbols(self_x: int, self_y: int, self_l: int) -> set[str]:
		x_0 = max(0, self_x - self_l)
		y_0 = max(0, self_y - 1)
		x_1 = min(schema_length, self_x + 1)
		y_1 = min(schema_height, self_y + 1)

		return set(
			lines[y_0][x_0 : x_1 + 1]
			+ lines[self_y][x_0 : x_1 + 1]
			+ lines[y_1][x_0 : x_1 + 1]
		)

	part_numbers_sum = 0

	for y, line in enumerate(lines):
		number_chunk = ""
		for x, char in enumerate(line):
			if char.isdigit():
				number_chunk += char

				if x == schema_length or not line[x + 1].isdigit():
					nearest_symbols = _get_nearest_symbols(x, y, len(number_chunk))

					if SYMBOLS.intersection(nearest_symbols):
						part_numbers_sum += int(number_chunk)

					number_chunk = ""

	return part_numbers_sum


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

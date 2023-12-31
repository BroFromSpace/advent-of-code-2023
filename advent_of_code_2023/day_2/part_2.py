from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

CHUNK_END_CHARS = {":", ";", ",", "\n"}


@pretty_output(title="Day 2: Cube Conundrum - Part 2", caption="part - 2")
def solution(lines: list[str]) -> int:
	cubes_power_sum = 0

	for line in lines:
		line = line.lower()
		word_chunk = ""
		number_chunk = ""

		max_rgb = {"red": 0, "green": 0, "blue": 0}

		for char in line:
			if char in CHUNK_END_CHARS:
				if word_chunk in max_rgb:
					max_rgb[word_chunk] = max(max_rgb[word_chunk], int(number_chunk))

				word_chunk = ""
				number_chunk = ""
			elif char.isalpha():
				word_chunk += char
			elif char.isdigit():
				number_chunk += char

		cubes_power_sum += max_rgb["red"] * max_rgb["blue"] * max_rgb["green"]

	return cubes_power_sum


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

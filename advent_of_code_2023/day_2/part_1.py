from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

MAX_CUBES_PER_COLOR = {"red": 12, "green": 13, "blue": 14}

CHUNK_END_CHARS = {":", ";", ",", "\n"}


@pretty_output(title="Day 2: Cube Conundrum - Part 1", caption="part - 1")
def solution(lines: list[str]) -> int:
	game_ids_sum = 0

	for line in lines:
		line = line.lower()
		game_id = 0
		word_chunk = ""
		number_chunk = ""

		for char in line:
			if char in CHUNK_END_CHARS:
				if word_chunk == "game":
					game_id = int(number_chunk)
				elif (
					word_chunk in MAX_CUBES_PER_COLOR
					and int(number_chunk) > MAX_CUBES_PER_COLOR[word_chunk]
				):
					game_id = 0

				word_chunk = ""
				number_chunk = ""
			elif char.isalpha():
				word_chunk += char
			elif char.isdigit():
				number_chunk += char

		game_ids_sum += game_id

	return game_ids_sum


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

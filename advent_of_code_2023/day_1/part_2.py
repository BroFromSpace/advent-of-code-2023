from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

LETTERS_TO_DIGITS = {
	"one": 1,
	"two": 2,
	"three": 3,
	"four": 4,
	"five": 5,
	"six": 6,
	"seven": 7,
	"eight": 8,
	"nine": 9,
}


@pretty_output(title="Day 1: Trebuchet?! - Part 2", caption="part - 2")
def solution(lines: list[str]) -> int:
	calibration_sum = 0

	for line in lines:
		first_number, last_number = None, None

		for i, char in enumerate(line):
			if char.isdigit():
				if first_number is None:
					first_number = int(char)
				last_number = int(char)
			else:
				if i < len(line) - 2 and line[i : i + 3] in LETTERS_TO_DIGITS:
					if first_number is None:
						first_number = LETTERS_TO_DIGITS[line[i : i + 3]]
					last_number = LETTERS_TO_DIGITS[line[i : i + 3]]
					continue
				if i < len(line) - 3 and line[i : i + 4] in LETTERS_TO_DIGITS:
					if first_number is None:
						first_number = LETTERS_TO_DIGITS[line[i : i + 4]]
					last_number = LETTERS_TO_DIGITS[line[i : i + 4]]
					continue
				if i < len(line) - 4 and line[i : i + 5] in LETTERS_TO_DIGITS:
					if first_number is None:
						first_number = LETTERS_TO_DIGITS[line[i : i + 5]]
					last_number = LETTERS_TO_DIGITS[line[i : i + 5]]
					continue

		calibration_sum += (
			int(f"{first_number}{last_number}") if first_number and last_number else 0
		)

	return calibration_sum


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

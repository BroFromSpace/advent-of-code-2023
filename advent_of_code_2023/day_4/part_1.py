from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


@pretty_output(title="Day 4: Scratchcards - Part 1", caption="part - 1")
def solution(lines: list[str]) -> int:
	total_points = 0

	for line in lines:
		points_per_card = 0
		winning_numbers, my_numbers = line.split("|")

		winning_set = set(winning_numbers.split())
		my_set = set(my_numbers.split())

		for _ in winning_set.intersection(my_set):
			if not points_per_card:
				points_per_card = 1
			else:
				points_per_card *= 2

		total_points += points_per_card

	return total_points


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

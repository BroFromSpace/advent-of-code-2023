from collections import defaultdict

from advent_of_code_2023.decorators import pretty_output


@pretty_output(title="Day 4: Scratchcards - Part 2")
def get_total_points(lines: list[str]) -> int:
    total_points = 0
    scratchcard_points = defaultdict(int)

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
    with open("./input.txt", "r", encoding="utf-8") as f:
        get_total_points(f.readlines())


if __name__ == "__main__":
    main()

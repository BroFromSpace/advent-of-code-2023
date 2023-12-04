from advent_of_code_2023.decorators import pretty_output


@pretty_output(title="Day 4: Scratchcards - Part 1")
def get_total_points(lines: list[str]) -> int:
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
    with open("./input.txt", "r", encoding="utf-8") as f:
        get_total_points(f.readlines())


if __name__ == "__main__":
    main()

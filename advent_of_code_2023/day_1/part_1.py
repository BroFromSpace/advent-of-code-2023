from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


@pretty_output(title="Day 1: Trebuchet?! - Part 1")
def solution(lines: list[str]) -> int:
    calibration_sum = 0

    for line in lines:
        first_number, last_number = None, None

        for char in line:
            if char.isdigit():
                if first_number is None:
                    first_number = char
                last_number = char

        calibration_sum += int(f"{first_number}{last_number}") if first_number and last_number else 0
    return calibration_sum


def main() -> None:
    solution(get_input_as_lines(Path('./input.txt')))


if __name__ == "__main__":
    main()

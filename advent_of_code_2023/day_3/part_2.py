from pathlib import Path
from collections import defaultdict

from advent_of_code_2023.utils import get_input_as_lines, pretty_output


@pretty_output(title="Day 3: Gear Ratios - Part 2")
def solution(lines: list[str]) -> int:
    schema_height = len(lines) - 1
    schema_length = len(lines[0]) - 1

    def _find_gear_positions(self_x: int, self_y: int, self_l: int) -> set[tuple[int, int]]:
        x_0 = max(0, self_x - self_l)
        y_0 = max(0, self_y - 1)
        x_1 = min(schema_length, self_x + 2)
        y_1 = min(schema_height, self_y + 2)

        return {
            (y, x) for y in range(y_0, y_1)
            for x in range(x_0, x_1) if lines[y][x] == "*"
        }

    gear_pos_num_map = defaultdict(list)

    for y, line in enumerate(lines):
        number_chunk = ""
        for x, char in enumerate(line):
            if char.isdigit():
                number_chunk += char

                if x == schema_length or not line[x + 1].isdigit():
                    for position in _find_gear_positions(x, y, len(number_chunk)):
                        gear_pos_num_map[position].append(int(number_chunk))

                    number_chunk = ""

    return sum((v[0] * v[1] for v in gear_pos_num_map.values() if len(v) == 2))


def main() -> None:
    solution(get_input_as_lines(Path('./input.txt')))


if __name__ == "__main__":
    main()

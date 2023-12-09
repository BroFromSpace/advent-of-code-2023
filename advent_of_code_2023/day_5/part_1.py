from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 5: If You Give A Seed A Fertilizer", caption="part - 1")
def solution(lines: str) -> int:
	seeds, *blocks = lines.split("\n\n")

	seeds = list(map(int, seeds.split(":")[1].split()))

	for block in blocks:
		ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]

		new = []
		for seed in seeds:
			for dest_range_start, src_range_start, range_len in ranges:
				if src_range_start <= seed < src_range_start + range_len:
					new.append(seed - src_range_start + dest_range_start)
					break
			else:
				new.append(seed)
		seeds = new

	return min(seeds)


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

from pathlib import Path

from advent_of_code_2023.utils import get_input_as_content, pretty_output


@pretty_output(title="Day 5: If You Give A Seed A Fertilizer", caption="part - 2")
def solution(lines: str) -> int:
	inputs_str, *blocks = lines.split("\n\n")
	inputs = list(map(int, inputs_str.split(":")[1].split()))

	seeds = []

	for i in range(0, len(inputs), 2):
		seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

	for block in blocks:
		ranges = [list(map(int, line.split())) for line in block.splitlines()[1:]]
		new = []
		while len(seeds) > 0:
			start_range, end_range = seeds.pop()
			for dest_range_start, src_range_start, range_len in ranges:
				o_start = max(start_range, src_range_start)
				o_end = min(end_range, src_range_start + range_len)
				if o_start < o_end:
					new.append(
						(
							o_start - src_range_start + dest_range_start,
							o_end - src_range_start + dest_range_start,
						)
					)
					if o_start > start_range:
						seeds.append((start_range, o_start))
					if start_range > o_end:
						seeds.append((o_end, end_range))
					break
			else:
				new.append((start_range, end_range))
		seeds = new

	return min(seeds)[0]


def main() -> None:
	solution(get_input_as_content(Path("./input.txt")))


if __name__ == "__main__":
	main()

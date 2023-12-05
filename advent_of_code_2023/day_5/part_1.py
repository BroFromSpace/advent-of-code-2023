from advent_of_code_2023.decorators import pretty_output


@pretty_output(title="title")
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
    with open("./input.txt", "r", encoding="utf-8") as f:
        solution(f.read())


if __name__ == "__main__":
    main()

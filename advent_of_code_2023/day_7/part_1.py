from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

LETTER_MAP = {"T": "A", "J": "B", "Q": "C", "K": "D", "A": "E"}


def classify(hand: str) -> int:
	counts = [hand.count(card) for card in hand]

	if 5 in counts:
		return 6
	if 4 in counts:
		return 5
	if 3 in counts:
		if 2 in counts:
			return 4
		return 3
	if counts.count(2) == 4:
		return 2
	if 2 in counts:
		return 1
	return 0


def strength(hand: str) -> tuple[int, list[str]]:
	return (classify(hand), [LETTER_MAP.get(char, char) for char in hand])


@pretty_output(title="Day 7: Camel Cards", caption="part - 1")
def solution(lines: list[str]) -> int:
	total = 0
	plays: list[tuple[str, int]] = []

	for line in lines:
		hand, bid = line.split()
		plays.append((hand, int(bid)))

	plays.sort(key=lambda play: strength(play[0]))

	for rank, (_, bid) in enumerate(plays, 1):  # type: ignore
		total += rank * bid  # type: ignore

	return total


def main() -> None:
	solution(get_input_as_lines(Path("./input.txt")))


if __name__ == "__main__":
	main()

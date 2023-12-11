from pathlib import Path

from advent_of_code_2023.utils import get_input_as_lines, pretty_output

LETTER_MAP = {"T": "A", "J": ".", "Q": "C", "K": "D", "A": "E"}


# Using brute-force
def score(hand: str) -> int:
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


def replacements(hand: str) -> list[str]:
	if hand == "":
		return [""]

	return [
		x + y
		for x in ("23456789TQKA" if hand[0] == "J" else hand[0])
		for y in replacements(hand[1:])
	]


def classify(hand: str) -> int:
	return max(map(score, replacements(hand)))


# Optimized method using math(~100x faster)
def opt_classify(hand: str) -> int:
	if hand == "JJJJJ":
		return 6

	counts = [0, *[hand.count(card) for card in hand if card != "J"]]
	num_jokers = hand.count("J")

	curr_max = max(counts)
	new_max = max(counts) + num_jokers

	num_max = curr_max
	for i, count in enumerate(counts):
		if num_max > 0 and count == curr_max:
			counts[i] = new_max
			num_max -= 1

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
	return (opt_classify(hand), [LETTER_MAP.get(char, char) for char in hand])


@pretty_output(title="Day 7: Camel Cards", caption="part - 2")
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

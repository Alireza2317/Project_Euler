from dataclasses import dataclass


RANKS = (
	'2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A'
)

def card_value(card_rank: str):
	return RANKS.index(card_rank)


@dataclass
class Card:
	rank: str
	suit: str

	def __repr__(self):
		return f'{self.rank}{self.suit}'


class Hand:
	def __init__(self, hand_s: str):
		self.cards: list[Card] = []

		for card_s in hand_s.split(' '):
			self.cards.append(
				Card(card_s[0], card_s[1])
			)

		self.sort()

	@staticmethod
	def card_value(card: Card):
		return RANKS.index(card.rank)

	def sort(self):
		self.cards.sort(key=self.card_value)


	def __repr__(self):
		return str(self.cards)


def read_poker_file() -> list[tuple[Hand, Hand]]:
	with open('poker.txt', 'r') as file:
		poker_content = file.read().split('\n')

	poker_games = [
		(Hand(game[:14]), Hand(game[15:]))
		for game in poker_content
	]

	return poker_games


def is_royal_flush(hand: Hand) -> bool:
	common_suit = hand.cards[0].suit

	for i, card in enumerate(hand.cards, RANKS.index('T')):
		if card_value(card.rank) != i:
			return False
		if card.suit != common_suit:
			return False

	return True

def is_straight(hand: Hand) -> bool:
	start_rank: str = hand.cards[0].rank
	start_rank_val = card_value(start_rank)

	for i, card in enumerate(hand.cards[1:], start_rank_val+1):
		if card_value(card.rank) != i:
			return False

	return True

def is_flush(hand: Hand) -> bool:
	common_suit = hand.cards[0].suit
	for card in hand.cards[1:]:
		if card.suit != common_suit:
			return False

	return True

def is_straight_flush(hand: Hand) -> bool:
	return is_straight(hand) and is_flush(hand)

def is_four_of_a_kind(hand: Hand) -> bool:
	ctr = 0
	common_rank: str = hand.cards[2].rank # middle card

	for card in hand.cards:
		if card.rank == common_rank:
			ctr += 1

	if ctr == 4:
		return True

	return False

def is_three_of_a_kind(hand: Hand) -> bool:
	ctr = 0
	common_rank: str = hand.cards[2].rank # middle card

	for card in hand.cards:
		if card.rank == common_rank:
			ctr += 1

	if ctr == 3:
		return True

	return False

def is_one_pair(hand: Hand) -> bool:
	if is_three_of_a_kind(hand) or is_four_of_a_kind(hand):
		return False

	ctr = 0
	for i in range(5):
		for j in range(i+1, 5):
			if hand.cards[i].rank == hand.cards[j].rank:
				ctr += 1

	if ctr == 1:
		return True

	return False

def is_two_pair(hand: Hand) -> bool:
	if is_three_of_a_kind(hand) or is_four_of_a_kind(hand):
		return False

	ctr = 0
	for i in range(5):
		for j in range(i+1, 5):
			if hand.cards[i].rank == hand.cards[j].rank:
				ctr += 1

	if ctr == 2:
		return True

	return False

def is_full_house(hand: Hand) -> bool:
	if not is_three_of_a_kind(hand):
		return False

	common_rank: str = hand.cards[2].rank

	left_indices = list(range(5))
	for i, card in enumerate(hand.cards):
		if card.rank == common_rank:
			left_indices.remove(i)

	card1 = hand.cards[left_indices[0]]
	card2 = hand.cards[left_indices[1]]

	if card1.rank == card2.rank:
		return True

	return False


def calculate_hand_mark(hand: Hand) -> int:
	mark: int = 0

	if is_royal_flush(hand):
		mark += 256

	if is_straight_flush(hand):
		mark += 128

	if is_four_of_a_kind(hand):
		mark += 64

	if is_full_house(hand):
		mark += 32

	if is_flush(hand):
		mark += 16

	if is_straight(hand):
		mark += 8

	if is_three_of_a_kind(hand):
		mark += 4

	if is_two_pair(hand):
		mark += 2


	if is_one_pair(hand):
		mark += 1

	return mark

def calculate_hand_extra_marks(hand: Hand) -> int:
	high_card_val = card_value(hand.cards[-1].rank)
	xmark: int = 0

	if is_royal_flush(hand):
		xmark += 0

	if is_straight_flush(hand) or is_flush(hand) or is_straight(hand):
		xmark += high_card_val

	if is_four_of_a_kind(hand):
		xmark += card_value(hand.cards[2].rank)

		first = card_value(hand.cards[0].rank)
		xmark += max(first, high_card_val)

	if is_full_house(hand) or is_three_of_a_kind(hand):
		threes_rank = card_value(hand.cards[2].rank)
		xmark += threes_rank*10

		second = card_value(hand.cards[1].rank)
		if second != threes_rank:
			xmark += second
		elif high_card_val != threes_rank:
			xmark += high_card_val


	if is_two_pair(hand):
		penultimate = card_value(hand.cards[-2].rank)
		xmark += penultimate*10
		xmark += card_value(hand.cards[1].rank)

	if is_one_pair(hand):
		pair_rank: str = hand.cards[0].rank
		for card in hand.cards[1:]:
			if card.rank == pair_rank:
				break
			else:
				pair_rank = card.rank

		xmark += card_value(pair_rank)*10

		if card_value(pair_rank) == high_card_val:
			xmark += card_value(hand.cards[-3].rank)
		else:
			xmark += high_card_val

	if xmark == 0:
		xmark += high_card_val

	return xmark

def who_wins(player1_hand: Hand, player2_hand: Hand) -> int:
	"""Returns either 1 or 2."""

	player1_mark = calculate_hand_mark(player1_hand)
	player2_mark = calculate_hand_mark(player2_hand)

	if player1_mark > player2_mark:
		return 1
	elif player2_mark > player1_mark:
		return 2

	# equal marks
	p1_xmarks = calculate_hand_extra_marks(player1_hand)
	p2_xmarks = calculate_hand_extra_marks(player2_hand)
	if p1_xmarks > p2_xmarks:
		return 1

	return 2


ctr = 0
for p1_hand, p2_hand in read_poker_file():
	if who_wins(p1_hand, p2_hand) == 1:
		ctr += 1

print(ctr)
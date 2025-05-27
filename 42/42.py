import string
from itertools import count

# tn = 0.5 * n * (n+1)
def tri_num(n: int) -> int:
	if n < 1: return None

	return 0.5 * n * (n+1)

def is_triangle_num(number: int) -> bool:
	for n in count(1):
		if tri_num(n) == number:
			return True
		elif tri_num(n) > number:
			return False


def read_words_file() -> list[str]:
	with open('words.txt', 'r') as file:
		content = file.read()

	return [
		quoted_word.removeprefix('"').removesuffix('"')
		for quoted_word in content.split(',')
	]


def is_triangle_word(word: str) -> bool:
	word_value: int = 0
	for character in word:
		char_value = string.ascii_uppercase.index(character)+1
		word_value += char_value

	if is_triangle_num(word_value):
		return True

	return False


count_triangle_words: int = 0

for word in read_words_file():
	if is_triangle_word(word):
		count_triangle_words += 1

print(count_triangle_words)
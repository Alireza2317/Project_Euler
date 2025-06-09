from itertools import permutations
import string


def read_file() -> list[int]:
	with open('cipher.txt') as file:
		enctypted_characters: list[int] = [
			int(s) for s in	file.read().split(',')
		]
	return enctypted_characters


def construct_full_key(key: str, length: int) -> str:
	key_len: int = len(key)
	if key_len > length: return

	full_key: list[int] = []

	for i in range(length):
		value: int = ord(key[i%key_len])
		full_key.append(value)

	full_key_s = [chr(i) for i in full_key]

	key_s: str = ''.join(full_key_s)

	return key_s


def encrypt(messg: str, key: str) -> str:
	fkey: str = construct_full_key(key, len(messg))

	e_msg: str = ''
	for i in range(len(messg)):
		echar_val = ord(fkey[i]) ^ ord(messg[i])
		e_msg += chr(echar_val)

	return e_msg


def is_valid(messg: str) -> bool:
	L = len(messg)
	words = messg.split()

	longest = max(words, key=len)
	if len(longest) > 25: return False

	letter_digit_count = 0
	for char in messg:
		if char in string.ascii_letters + string.digits:
			letter_digit_count += 1

	if letter_digit_count > 0.7 * L:
		return True

	return False



enctypted_characters: list[int] = read_file()
enctypted_message =  ''.join([chr(i) for i in enctypted_characters])

for perm in permutations(string.ascii_lowercase, r=3):
	key = ''.join(perm)

	dec_mssg = encrypt(enctypted_message, key)

	if is_valid(dec_mssg):
		original_messg = dec_mssg
		break

s = 0
for char in original_messg:
	s += ord(char)

print(s)
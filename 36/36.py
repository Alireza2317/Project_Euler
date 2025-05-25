def is_palindrome(number: int):
	s = str(number)
	i = 0
	while s:
		if len(s) == 1:	return True

		if s[i] != s[-(i+1)]:
			return False

		s = s[i+1:-(i+1)]

	return True


def is_palindrome_10and2(number: int):
	number_binary: str = bin(number).removeprefix('0b')
	if is_palindrome(number) and is_palindrome(number_binary):
		return True
	return False


s: int = 0
for number in range(1, 1_000_000):
	if is_palindrome_10and2(number):
		s += number

print(s)

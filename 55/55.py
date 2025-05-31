def is_palindrome(number: int) -> bool:
	if str(number) == ''.join(reversed(str(number))):
		return True

	return False

def reverse(number: int) -> int:
	return int(''.join(reversed(str(number))))


def is_lychrel(number: int) -> bool:
	num = number
	for _ in range(50):
		num += reverse(num)
		if is_palindrome(num):
			return False

	return True



ctr = 0

for num in range(1, 10_000):
	if is_lychrel(num):
		ctr += 1

print(ctr)
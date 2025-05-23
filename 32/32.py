# an n-digit number is pandigital if
# it makes use of all the digits 1 to n exactly once

def get_digits(number: int) -> list[int]:
	return [int(digit_str) for digit_str in str(number)]

def has_duplicate_digits(number: int) -> bool:
	digits: list[int] = get_digits(number)
	if len(digits) == len(set(digits)):
		return False

	return True

def is_mult_pandigital_1to9(num1: int, num2: int, product: int) -> bool:
	s = f'{num1}{num2}{product}'
	if len(s) != 9: return False
	if '0' in s: return False

	n: int = int(s)

	if not has_duplicate_digits(n):
		return True

	return False



products = set()

for a in range(1, 9877):
	for b in range(1, a):
		p = a * b
		if is_mult_pandigital_1to9(a, b, p):
			products.add(p)
			print(f'{a}*{b} = {p}')



print(sum(products))
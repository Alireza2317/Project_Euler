from itertools import count

# an n-digit number is pandigital if
# it makes use of all the digits 1 to n exactly once

def get_digits(number: int) -> list[int]:
	return [int(digit_str) for digit_str in str(number)]

def has_duplicate_digits(number: int) -> bool:
	digits: list[int] = get_digits(number)
	if len(digits) == len(set(digits)):
		return False

	return True

def is_pandigital_1to9(number: int) -> bool:
	number_s = str(number)
	if len(number_s) != 9: return False
	if '0' in number_s: return False


	if not has_duplicate_digits(number):
		return True

	return False

def concat_product(number: int, n: int) -> int:
	result: str = ''

	for n in range(1, n+1):
		result += str(n*number)

	result_int = int(result)

	return result_int


max_num: int = -1

# we should know that number should be below 10_000 since it (at least) doubles
# in size of digits, and if it is bigger than 10_000 it will go beyond 9 digits
for number in range(2, 10_000):
	for n in count(2):
		x = concat_product(number, n)
		if len(str(x)) > 9: break

		if is_pandigital_1to9(x):
			if x > max_num:
				max_num = x
				info = (number, n)

print(max_num)


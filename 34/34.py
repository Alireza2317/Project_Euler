from functools import cache
import time

def get_digits(number: int) -> list[int]:
	return [int(digit_str) for digit_str in str(number)]


def factorial(number: int) -> int:
	if number in (0, 1): return 1

	f: int = 1
	for i in range(2, number+1):
		f *= i

	return f


def sum_digits_factorical(number: int):
	digits = get_digits(number)

	s = 0
	for d in digits:
		s += factorial(d)

	return s

s = 0
for number in  range(10, 9999999):
	sdf = sum_digits_factorical(number)
	if sdf > len(get_digits(number))*factorial(9): break

	if number == sdf:
		s += number
print(s)
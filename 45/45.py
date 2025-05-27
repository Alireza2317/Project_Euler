from math import sqrt
from itertools import count

def pent_num(n: int) -> int:
	return n * (3*n - 1) // 2


def is_triangle(number: int) -> bool:
	delta = 1 + 8*number
	n = (sqrt(delta) - 1) / 2

	return n == int(n)


def is_hexagonal(number: int) -> bool:
	delta = 1 + 8*number

	n = (1 + sqrt(delta)) / 4

	return n == int(n)


for n in count(166):
	p = pent_num(n)

	if is_triangle(p) and is_hexagonal(p):
		print(p)
		exit()

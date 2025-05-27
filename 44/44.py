from itertools import count
from math import sqrt

def pentagonal_num(n: int) -> int:
	return n * (3*n - 1) // 2


def is_pentagonal(number: int) -> bool:
	delta = 1 + 24*number

	n = (1 + sqrt(delta)) / 6

	return n == int(n)


for i in count(2):
	for j in range(1, i):
		p_i = pentagonal_num(i)
		p_j = pentagonal_num(j)

		D = p_i - p_j
		s = p_i + p_j

		if is_pentagonal(D) and is_pentagonal(s):
			print(D)
			exit()

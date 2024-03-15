from math import floor, sqrt
import itertools
import time
def tri_num(n: int) -> int:
	# using the algebraic formula directly to calculate 1+2+...+n
	return n * (n+1) // 2


def count_divisors(n: int) -> int:
	count: int = 2;
	sqrt_n: int = floor(sqrt(n))
	for i in range(2, sqrt_n + 1):
		if n%i == 0: count += 2;
	
	if sqrt_n ** 2 == n: count -= 1

	return count


for num in itertools.count(1):
	if count_divisors(tri_num(num)) > 500:
		print(tri_num(num))
		break

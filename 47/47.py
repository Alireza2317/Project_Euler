import math
from itertools import count

def is_prime(n):
	if n == 1: return False
	if n == 2: return True

	for i in range(2, math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False

	return True


def prime_factors(number: int) -> set[int]:
	factors = set()
	factor = 2

	while True:
		if number%factor == 0:
			factors.add(factor)
			number //= factor

			if number < 2: break
		else:
			factor += 1


	return factors

threshold: int = 4
ctr: int = 0


for num in count(647):
	if len(prime_factors(num)) == threshold:
		ctr += 1
	else:
		ctr = 0

	if ctr == threshold:
		for i in range(threshold-1, -1, -1):
			print(f'{num-i}: {prime_factors(num-i)}')
		break
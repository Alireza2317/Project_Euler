from math import ceil, sqrt
import itertools

def is_prime(n: int) -> bool:
	if n == 2: return True

	for i in range(2, ceil(sqrt(n))+1):
		if n % i == 0: return False

	return True


def primes(n: int) -> int:
	if n == 1: return 2

	count: int = 1
	for i in itertools.count(3, 2):
		if is_prime(i): count += 1
		if count == n: return i


n: int = 10001
print(primes(n))

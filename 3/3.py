from math import sqrt, ceil

def is_prime(n: int) -> bool:
	if n == 1: return False
	if n == 2: return True

	for i in range(2, ceil(sqrt(n))+1):
		if n%i == 0:
			return False

	return True


def biggest_prime_factor(n: int) -> int:
	if is_prime(n): return n

	for i in range(ceil(sqrt(n)), 2, -1):
		if n%i: continue
		if is_prime(i): return i


n: int = 600851475143

print(biggest_prime_factor(n))
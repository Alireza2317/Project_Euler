from math import ceil, sqrt

def is_prime(n: int) -> bool:
	if n == 2: return True

	for i in range(2, ceil(sqrt(n))+1):
		if n % i == 0: return False

	return True

sum_primes: int = 2
for i in range(3, 2_000_000, 2):
	if is_prime(i):
		sum_primes += i


print(sum_primes)
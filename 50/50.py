import math
from itertools import count

def is_prime(number: int) -> bool:
	if number in (0, 1): return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True


def primes(start: int, end: int):
	for n in count(start):
		if n >= end: break

		if is_prime(n):
			yield n


primes_tuple = tuple(primes(2, 1_200_000))

max_len = 0
prime = 0
saved_i = 0

for start_i in range(len(primes_tuple)):
	for chain_len in range(2, len(primes_tuple)+1):
		s = sum(primes_tuple[start_i:start_i+chain_len])
		if s >= 1_000_000: break

		if not is_prime(s): continue

		if chain_len > max_len:
			max_len = chain_len
			prime = s
			saved_i = start_i

print(prime)
print(f'lenth = {max_len}, starting from: {primes_tuple[saved_i]}')


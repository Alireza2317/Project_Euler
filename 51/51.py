import math
from itertools import count

def is_prime(number: int) -> bool:
	if number == 1: return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True


def select_digits_indices(number_len: int, n: int) -> list[set[int]]:
	"""
	Returns a list of sets
	each set contains indices
	"""
	if n >= number_len: return None

	results = []

	for binary_n in range(1, 2**number_len - 1):
		bn = bin(binary_n).removeprefix('0b').zfill(number_len)
		if bn.count('1') != n: continue

		indices: set[int] = set()

		for i, b in enumerate(bn):
			if b == '1': indices.add(i)

		results.append(indices)

	return results


def change_prime(prime: int, indices: set[int]) -> list[int]:
	results: list[int] = []

	p_s: str = str(prime)

	for fill_digit in range(10):
		# 0 can be filled if 0 is not in indices
		if (0 in indices) and (fill_digit == 0): continue

		for index in indices:
			#p_s[index] = str(fill_digit)
			p_s = f'{p_s[:index]}{fill_digit}{p_s[index+1:]}'

		results.append(int(p_s))

	return results


def count_primes(list_of_nums: list[int]) -> int:
	ctr: int = 0
	for num in list_of_nums:
		if is_prime(num):
			ctr += 1

	return ctr


for number in count(100):
	if not is_prime(number): continue

	number_len = len(str(number))
	for n in range(1, number_len):
		for indices in select_digits_indices(number_len, n):
			new_nums = change_prime(number, indices)

			c: int = count_primes(new_nums)

			if c >= 8:
				print(min(new_nums))
				exit()
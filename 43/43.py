import string
from itertools import permutations


def has_property(number_s: str) -> bool:
	primes: list[int] = [2, 3, 5, 7, 11, 13, 17]

	for i in range(1, 8):
		sub_num = int(number_s[i:i+3])

		if not (sub_num % primes[i-1] == 0):
			return False

	return True


s: int = 0

for perm in permutations(string.digits):
	if perm[0] == '0': continue

	num_s: str = ''.join(perm)

	if has_property(num_s):
		s += int(num_s)

print(s)
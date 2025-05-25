import math
from itertools import permutations
import string

def is_prime(n):
	if n == 1: return False
	if n == 2: return True

	for i in range(2, math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False

	return True


# since every 9-digit and 8-digit numbers are divisable by 9
# they cannot be prime
for n in range(7, 1, -1):
	digits = string.digits[n:0:-1]
	for permutation in permutations(digits):
		number = int(''.join(permutation))
		if is_prime(number):
			print(number)
			exit()

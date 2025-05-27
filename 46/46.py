import math
from itertools import count

def is_prime(n):
	if n == 1: return False
	if n == 2: return True

	for i in range(2, math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False

	return True


def is_square(number: int) -> bool:
	if number == 1: return True

	c: int = 0
	for i in range(2, number):
		if number%i == 0:
			c += 1

	if c%2 == 1: return True

	return False


for number in count(33, step=2):
	if is_prime(number): continue

	# check all primes less than the number
	for smaller_num in range(3, number-1):

		if not is_prime(smaller_num): continue

		# smaller_num is the prime
		sq = number - smaller_num

		sq //= 2

		if is_square(sq):
			base = int(math.sqrt(sq))
			print(f'{number} = {smaller_num} + 2*{base}²')
			break
	else:
		print(number)
		break
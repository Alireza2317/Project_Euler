# n^2 + an + b
import math


def is_prime(number):
	if number in (0, 1): return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True



max_len = 0
coeffs = []

for a in range(-999, 1000):
	if a==0: continue
	for b in range(-1000, 1001):
		if a**2 > 4*b: continue
		if not is_prime(b): continue

		n = 0
		counter = 0
		while True:
			check_number = n**2 + a*n + b

			if is_prime(check_number):
				counter += 1
			else:
				break

			n += 1

		if counter > max_len:
			max_len = counter
			coeffs = [a, b]


print(coeffs[0]*coeffs[1])
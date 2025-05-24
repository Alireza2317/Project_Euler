import math

def is_prime(number: int) -> bool:
	if number in (0, 1): return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True

def get_circulations(number: int) -> list[int]:
	circs: list[int] = []

	number_s: str = str(number)
	num_digits = len(number_s)

	for _ in range(num_digits):
		number_s = number_s[-1] + number_s[:-1]
		circs.append(int(number_s))

	return circs

def is_circular_prime(number: int) -> bool:
	circs = get_circulations(number)
	for num in circs:
		if not is_prime(num):
			return False
	return True


count: int = 0
for number in range(1_000_000):
	if is_circular_prime(number):
		count += 1

print(count)
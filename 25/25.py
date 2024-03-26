from functools import cache
import itertools

@cache
def fibonacci(n: int) -> int:
	if n == 1 or n == 2:
		return 1
	
	return fibonacci(n - 1) + fibonacci(n - 2)


def count_digits(n: int) -> int:
	count: int = 0
	while n:
		count += 1
		n //= 10
	return count


for i in itertools.count(1):
	if count_digits(fibonacci(i)) >= 1000:
		print(i)
		break
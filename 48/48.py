def get_last10_digits(number: int) -> int:
	return number % (10**10)


s: int = 0
for n in range(1, 1001):
	s += n**n

print(get_last10_digits(s))
def sum_digits(n : int):
	result: int = 0

	while n:
		result += n % 10
		n //= 10

	return result

number = 2 ** 1000
print(sum_digits(number))

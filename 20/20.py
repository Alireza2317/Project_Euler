def factorial(n: int)-> int:
	result: int = 1
	for i in range(2, n + 1):
		result *= i
	
	return result


def sum_digit(n: int) -> int:
	result: int = 0
	
	while n:
		result += (n % 10)
		n //= 10

	return result

print(sum_digit(factorial(100)))

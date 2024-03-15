def sum_proper_divisors(n: int) -> int:
	result = 0
	for i in range(1, n):
		if n % i == 0:
			result += i
	return result


def is_amicable(n: int) -> bool:
	s: int = sum_proper_divisors(n)

	if n == sum_proper_divisors(s):
		return True

	return False

sum_of_amicables = 0
for number in range(1, 10_001):
	if is_amicable(number):
		sum_of_amicables += number

print(sum_of_amicables)

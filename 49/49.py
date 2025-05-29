import math

def are_permutions(number1: int, number2: int) -> bool:
	number1_s = str(number1)
	number2_s = str(number2)

	if len(number1_s) != len(number2_s): return False

	result: bool = True

	for n_s in number1_s:
		if n_s not in number2_s:
			result = False

	for n_s in number2_s:
		if n_s not in number1_s:
			result = False


	return result


def is_prime(number: int) -> bool:
	if number in (0, 1): return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True


#print(are_permutions(1009, 1039))

for first_number in range(1488, 10_000):
	if not is_prime(first_number): continue

	second_number = first_number + 3330
	third_number = second_number + 3330

	if not are_permutions(first_number, second_number): continue
	if not are_permutions(first_number, third_number): continue

	if is_prime(second_number) and is_prime(third_number):
		break

print(f'{first_number}{second_number}{third_number}')
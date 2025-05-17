def digits(number):
	return [int(d) for d in str(number)]

def sum_fifth_powers(number):
	ds = digits(number)

	s = 0
	for d in ds:
		s += d**5

	return s

total_sum = 0

number = 10
while True:
	if number == sum_fifth_powers(number):
		total_sum += number

	elif len(digits(number)) * (9**5) < number:
		break

	number += 1

print(total_sum)
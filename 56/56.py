def sum_digits(number: int) -> int:
	s = 0
	while number:
		number, d = divmod(number, 10)
		s += d

	return s


max_sumd = 0
for a in range(1, 100):
	for b in range(1, 100):
		s = sum_digits(a**b)
		if s > max_sumd:
			max_sumd = s

print(max_sumd)
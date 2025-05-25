from itertools import count

number_s = ''
for i in count(1):
	number_s += str(i)
	if len(number_s) > 1_000_000:
		break

result = 1

for zeros in range(6):
	result *= int(number_s[10**zeros - 1])

print(result)
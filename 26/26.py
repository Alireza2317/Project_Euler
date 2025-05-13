def find_recurring_length(numerator, denominator):
    remainders = {}  # Dictionary to store remainders and their positions
    quotient = numerator // denominator
    remainder = numerator % denominator
    position = 0
    
    while remainder != 0 and remainder not in remainders:
        remainders[remainder] = position
        numerator = remainder * 10
        quotient = numerator // denominator
        remainder = numerator % denominator
        position += 1
    
    if remainder == 0:
        return 0  # No recurring part
    
    return position - remainders[remainder]
print(find_recurring_length(1, ))

maximum_recurring = 0
for d in range(2, 1000):
	count: int = find_recurring_length(1, d)
	if count > maximum_recurring:
		maximum_recurring = count
		answer = d

print(maximum_recurring)
print(d)

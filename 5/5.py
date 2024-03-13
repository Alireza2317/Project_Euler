def gcd(a: int, b: int) -> int:
	# make sure a is always bigger
	a, b = b, a
	
	rem = a % b
	while rem:
		# the new bigger number is the original smaller number (b)
		# and the new smaller number is the new remainder
		a = b
		b = rem
		rem = a % b

	# the last smaller number would be the gcm
	return b

def lcm(a: int, b: int) -> int: 
	return (a * b) // gcd(a, b)


p: int = 1

for i in range(2, 21):
	# find the lcm along the number line
	p = lcm(p, i)

print(p)
prod_numerators = 1
prod_denominators = 1

for denominator in range(11, 100):
	for numerator in range(10, denominator):
		num_s = str(numerator)
		den_s = str(denominator)

		# trivial
		if num_s[1] == den_s[1]: continue

		if num_s[0] == den_s[1]:
			num_s = num_s[1]
			den_s = den_s[0]

		elif num_s[1] == den_s[0]:
			num_s = num_s[0]
			den_s = den_s[1]

		elif num_s[0] == den_s[0]:
			num_s = num_s[1]
			den_s = den_s[1]

		else: continue

		if num_s == '0' or den_s == '0': continue


		if int(num_s) / int(den_s) == numerator/denominator:
			print(f'{numerator}/{denominator}')
			prod_numerators *= numerator
			prod_denominators *= denominator

print('______')
print(f'{prod_numerators}/{prod_denominators}')

num = prod_numerators
den = prod_denominators

num_divisors = set()
den_divisors = set()

for i in range(2, num+1):
	if num%i == 0:
		num_divisors.add(i)

for i in range(2, den+1):
	if den%i == 0:
		den_divisors.add(i)

commons = num_divisors.intersection(den_divisors)

gcd = max(commons)

den //= gcd
num //= gcd

print(f'{num}/{den}')
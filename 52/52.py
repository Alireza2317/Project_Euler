from itertools import count

def have_same_digits(num1: int, num2: int) -> bool:
	num1_s: str = str(num1)
	num2_s: str = str(num2)

	if len(num1_s) != len(num2_s): return False

	for d_s in num1_s:
		if d_s not in num2_s: return False

	for d_s in num2_s:
		if d_s not in num1_s: return False

	return True



for num in count(1):
	a = num*2
	b = num*3
	c = num*4
	d = num*5
	e = num*6

	if not have_same_digits(num, a): continue
	if not have_same_digits(a, b): continue
	if not have_same_digits(b, c): continue
	if not have_same_digits(c, d): continue
	if not have_same_digits(d, e): continue

	print(num, a, b, c, d, e)
	break

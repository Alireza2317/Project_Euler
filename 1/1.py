def is_divisable_5or3(n: int) -> bool:
	if n%3 == 0 or n%5 == 0:
		return True
	return False


n: int = 1000
s: int = 0

for i in range(1, 1000):
	if is_divisable_5or3(i):
		s += i

print(s)
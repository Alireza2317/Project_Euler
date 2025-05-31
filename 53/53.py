def factorial(n: int) -> int:
	if n in (0, 1): return 1

	f: int = 1
	for i in range(2, n+1):
		f *= i

	return f


def n_combinations(r: int, n: int) -> int:
	if r > n: return None

	return factorial(n) // factorial(r) // factorial(n-r)


ctr: int = 0
for n in range(1, 101):
	for r in range(1, n+1):
		if n_combinations(r, n) > 1_000_000:
			ctr += 1

print(ctr)
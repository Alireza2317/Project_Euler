def permutations(items: list[str]):
	if len(items) == 0:
		yield []
	else:
		for i in range(len(items)):
			first_element = items[i]
			rest = permutations(items[:i] + items[i+1:])

			for perm in rest:
				yield [first_element] + perm

p = permutations('0123456789')

for i, perm in enumerate(p, 1):
	if i == 1_000_000:
		print(''.join(perm))
		break

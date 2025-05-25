def is_right_angle(a: int, b: int, hypotnuse: int) -> bool:
	if a**2 + b**2 == hypotnuse**2:
		return True

	return False

def possible_sides_for(perimeter: int) -> set[tuple[int, int, int]]:
	solutions: set[tuple[int, int, int]] = set()

	for side1 in range(1, perimeter):
		for side2 in range(1, perimeter):
			side3 = perimeter - side1 - side2
			if side1+side2+side3 != perimeter or side3 <= 0: continue

			sides = [side1, side2, side3]
			sides.sort()

			if is_right_angle(*sides):
				solutions.add(tuple(sides))

	return solutions

def count_right_triangles_for(perimeter: int) -> int:
	return len(possible_sides_for(perimeter))

max_solutions = 0
perimeter = 0
for p in range(4, 1001):
	c = count_right_triangles_for(p)
	if c > max_solutions:
		max_solutions = c
		perimeter = p


print(perimeter, possible_sides_for(perimeter))
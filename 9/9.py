def is_pythagorean(legs: list[int]) -> bool:
	hypotenuse = max(legs)
	
	# assign all legs except the hypotenuse to this variable
	#other_legs = legs[:]
	#other_legs.remove(hypotenuse)
	# this line below replaces the two lines above using the walrus operator
	(other_legs := legs[:]).remove(hypotenuse)

	
	if other_legs[0]** 2 + other_legs[1]**2 == hypotenuse**2:
		return True

	return False


def main():
	for a in range(1, 1000):
		for b in range(a + 1, 1000 - a):
			c = 1000 - a - b
			if is_pythagorean([a, b, c]):
				print(a * b * c)
				return

main()
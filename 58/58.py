import math
from itertools import count

directions = ('d', 'r','u', 'l')

def next_location(current_loc, direction):
	if direction == 'r':
		loc = (current_loc[0], current_loc[1]+1)
	elif direction == 'l':
		loc = (current_loc[0], current_loc[1]-1)
	elif direction == 'u':
		loc = (current_loc[0]-1, current_loc[1])
	elif direction == 'd':
		loc = (current_loc[0]+1, current_loc[1])

	return loc


def next_direction(current_direction):
	i = directions.index(current_direction)

	return directions[(i+1)%4]


def is_cell_empty(matrix, loc):
	return matrix[loc[0]][loc[1]] == 0


def is_square(number: int) -> bool:
	if number == 1: return True

	c: int = 0
	for i in range(2, number):
		if number%i == 0:
			c += 1

	if c%2 == 1: return True

	return False


def is_prime(number: int) -> bool:
	if number == 1: return False
	if number == 2: return True

	for i in range(2, math.ceil(math.sqrt(number))+1):
		if number%i == 0:
			return False

	return True

for n in count(7, 2):
	if not (n%2 == 1 and is_square(n)):
		continue

	matrix = [
		[0 for _ in range(n)]
		for _ in range(n)
	]


	start_loc = (n//2, n//2)
	loc = start_loc
	direction = directions[0]

	totals = 2*n - 1
	c_primes = 0

	for number in range(1, n**2+1):
		matrix[loc[0]][loc[1]] = number
		
		if (loc[0] == loc[1]) or (loc[0]+loc[1] == n-1):
			if is_prime(number):
				c_primes += 1

		next_dir = next_direction(direction)
		nl = next_location(loc, next_dir)

		if is_cell_empty(matrix, nl):
			direction = next_dir
			loc = nl
		else:
			loc = next_location(loc, direction)

	if c_primes/totals < 0.1:
		print(n)
		break

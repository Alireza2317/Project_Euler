directions = ('u', 'r', 'd', 'l')

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

N = 1001
matrix = [
	[0 for _ in range(N)]
	for _ in range(N)
]


start_loc = (N//2, N//2)
loc = start_loc
direction = directions[0]

for number in range(1, N**2+1):
	matrix[loc[0]][loc[1]] = number

	next_dir = next_direction(direction)
	nl = next_location(loc, next_dir)

	if is_cell_empty(matrix, nl):
		direction = next_dir
		loc = nl
	else:
		loc = next_location(loc, direction)

#for row in matrix:
#	for number in row:
#		print(f'{number:^4}', end='')
#	print()

s = 0
for row in range(N):
	for col in range(N):
		if (row == col) or (row+col == N-1):
			s += matrix[row][col]
print(s)
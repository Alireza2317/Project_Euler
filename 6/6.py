sum_of_squares: int = 0
squares_of_sum: int = 0
for i in range(1, 101):
	sum_of_squares += (i*i)
	squares_of_sum += i

squares_of_sum *= squares_of_sum
print(squares_of_sum - sum_of_squares)
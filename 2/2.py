from functools import cache
from itertools import count
import time

@cache
def fibonacci(n: int) -> int:
	if n <= 2:
		return n
	return fibonacci(n-1) + fibonacci(n-2)

def is_even(n: int) -> bool:
	if n%2 == 0:
		return True
	return False


# i came up with these two ways of solving this problem
# turns out that the second way takes about half the time
# the first way does

#s: int = 0
#i: int = 1
#while (fib := fibonacci(i)) <= 4_000_000:
#	if is_even(fib):
#		s += fib
#	i += 1


s: int = 0

for i in count(1):
	if (fib := fibonacci(i)) <= 4_000_000:
		if is_even(fib):
			s += fib

	else: break

print(s)
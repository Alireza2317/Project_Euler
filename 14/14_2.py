import time

def collatz_len(n):
	length = 0
	while True:
		if n == 1:
			#print(1)
			length += 1
			break

		# bigger than 1
		#print(int(n), end=' ')
		length += 1

		# even
		if n%2 == 0:
			n //= 2
		else: # odd
			n = n*3 + 1

	return length


limit = 1_000_000
max_len = 0

start_t = time.perf_counter()

for start_num in range(1, limit):
	l = collatz_len(start_num)
	if l > max_len:
		max_len = l

end_t = time.perf_counter()

print(max_len)
print(f'{end_t-start_t:.3f}')
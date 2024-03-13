def is_palindrome(n: int) -> bool:
	nd = n
	n_rev = 0

	while nd:
		n_rev *= 10
		n_rev += nd % 10
		nd //= 10

	if n == n_rev:
		return True
	return False	


N: int = 999;
M: int = 100;

for total in range(2*N, 2*M - 1, -1):
	for i in range(max(M, total - N), min(N, total - M) + 1):
		j = total - i
		
		if is_palindrome(i*j):
			print(i*j)
			exit()
			

import math

def is_prime(n):
	if n == 1: return False
	if n == 2: return True

	for i in range(2, math.ceil(math.sqrt(n))+1):
		if n%i == 0:
			return False

	return True

def strip_right(n):
	if n >= 10:
		return n//10
	else:
		return -1

def strip_left(n):
	if n >= 10:
		string = str(n)[1:]
		return int(string)
	else:
		return -1


def is_trunc(n):
	n2 = n
	n3 = n
	if not is_prime(n):
		return False

	# right stripping
	for i in range(len(str(n))-1):
		n2 = strip_right(n2)
		if not is_prime(n2):
			return False

	# left stripping
	for i in range(len(str(n))-1):
		n3 = strip_left(n3)
		if not is_prime(n3):
			return False

	return True

s = 0
for i in range(11, 800000):
	if is_trunc(i):
		s += i
print(s)



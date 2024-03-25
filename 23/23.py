import math
limit = 28123

def proper_divisors_sum(limit: int) -> list[int]:
	output = [1 for _ in range(limit)]
	for i in range(2, math.ceil(math.sqrt(limit))):
		for j in range(i, limit//i):
			if i == j:
				output[i*j] += i
			else:
				output[i*j] += (i+j)
	return output

def abundant_numbers(limit: int) -> list[int]:
	nums = []
	propdivs = proper_divisors_sum(limit)
	for num in range(12, limit):
		if propdivs[num] > num:
			nums.append(num)
		
	return nums

ab_nums: list[int] = abundant_numbers(limit)

# we first assume all the numbers within the limit qualify
# then we will remove the numbers that don't qualify 
not_summable_ab_nums: set[int] = set(range(limit))

for i in range(len(ab_nums)):
	for j in range(i, len(ab_nums)):
		sum_of_ab_nums = ab_nums[i] + ab_nums[j]
		if sum_of_ab_nums < limit: 
			# this number does not qualify because 
			# its a sum of two abundant numbers
			# clear the number that did not qualify
			if sum_of_ab_nums in not_summable_ab_nums:
				not_summable_ab_nums.remove(sum_of_ab_nums)
		else: 
			# we are above the required limit and we dont have to check
			break


print(sum(not_summable_ab_nums))
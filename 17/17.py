def count_without_spaces(number: str) -> int:
	return len(number) - number.count(' ')


def int_to_str(num: int) -> str:
	# this function works for n <= 1000
	if num > 1000:
		raise NotImplementedError('Please enter a number below 1000!')
	
	one_to_ten_digits = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
	eleven_to_nineteen_digits = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
	ten_multiples = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

	if num <= 10 and num > 0:
		return one_to_ten_digits[num - 1]
	
	if num > 10 and num < 20:
		return eleven_to_nineteen_digits[num-11]
	
	if num >= 20 and num < 100:
		s: str = ten_multiples[num // 10 - 2]
		if num % 10:
			ss: str = one_to_ten_digits[num % 10 - 1]
		else:
			ss = ' '

		return f'{s} {ss}'
	
	if num >= 100 and num < 1000:
		d: int = num // 100
		dd: int = (num // 10) % 10
		ddd: int = num % 10
		
		s = one_to_ten_digits[d - 1]
		ss = int_to_str(num % 100)

		if dd or ddd:
			return f'{s} hundred and {ss}'

		return f'{s} hundred'

	if num == 1000:
		return 'one thousand'


sum_leters = 0
for i in range(1, 1001):
	sum_leters += count_without_spaces(int_to_str(i))

print(sum_leters)
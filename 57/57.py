import math
from typing import Self
from functools import cache

class Fraction:
	def __init__(self, numerator: int, denominator: int):
		self.numerator: int = numerator
		self.denominator: int = denominator

		self.simplify()


	def simplify(self) -> None:
		g = math.gcd(self.numerator, self.denominator)

		self.numerator //= g
		self.denominator //= g


	@property
	def value(self) -> float:
		return self.numerator / self.denominator


	def __add__(self, other: Self | int) -> Self:
		if isinstance(other, int):
			other = Fraction(other, 1)

		l = math.lcm(self.denominator, other.denominator)

		modifier1 = l // self.denominator
		modifier2 = l // other.denominator

		self.numerator *= modifier1
		self.denominator = l

		other.numerator *= modifier2
		other.denominator = l

		result = Fraction(self.numerator+other.numerator, self.denominator)

		self.simplify()
		other.simplify()
		result.simplify()

		return result


	def __radd__(self, other: Self | int) -> Self:
		if isinstance(other, int):
			other = Fraction(other, 1)

		return (self + other)


	def __sub__(self, other: Self | int) -> Self:
		if isinstance(other, int):
			other = Fraction(other, 1)

		f = Fraction(-other.numerator, other.denominator)
		return (self + f)


	def __truediv__(self, other: Self | int) -> Self:
		if isinstance(other, int):
			other = Fraction(other, 1)

		n = self.numerator * other.denominator
		d = self.denominator * other.numerator

		return Fraction(n, d)


	def __rtruediv__(self, other: Self | int) -> Self:
		if isinstance(other, int):
			other = Fraction(other, 1)

		n = other.numerator * self.denominator
		d = other.denominator * self.numerator

		return Fraction(n, d)


	def __repr__(self):
		if self.denominator == 1:
			return f'[{self.numerator}]'

		return f'[{self.numerator}/{self.denominator}]'



def num_digits(number: int) -> int:
	d = 0
	while number:
		d += 1
		number //= 10

	return d


def sqrt2_rec(precision):
	@cache
	def inner_fraction(precision):
		if precision == 1:
			return Fraction(1, 2)

		return 1 / (2 + inner_fraction(precision-1))

	return 1 + inner_fraction(precision)


def sqrt2(precision):
	result: Fraction = Fraction(1, 2)

	for _ in range(2, precision+1):
		result = 1 / (2 + result)

	return 1 + result

ctr = 0
for p in range(1, 1001):
	sq = sqrt2(p)

	if num_digits(sq.numerator) > num_digits(sq.denominator):
		ctr += 1

print(ctr)
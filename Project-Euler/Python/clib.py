import datetime
from functools import reduce
from math import *
import inflect
from itertools import islice, permutations

# Allows for caching of calculations
# Usage:
#	@memorize
#	def func()
class memorize(object):
	def __init__(self, func):
		self.func = func
		self.cache = {}
		return None
	def __call__(self, *args):
		if args in self.cache:
			return self.cache[args]
		else:
			val = self.func(*args)
			self.cache[args] = val
			return val

# Determines of a number is a palindrome
def is_palindrome(number):
	return str(number) == str(number)[::-1]

# Determines if a number is divisible by all numbers 1 to 20
def is_smallest_multiple(number):
	for i in range(20, 2, -1):
		if number % i != 0:
			return False
	return True

# Determines if a number is prime
def is_prime(number):
	if (number % 2 == 0 and number > 2) or (number < 2):
		return False
	for i in range(3, int(sqrt(number)), 2):
		if number % i == 0:
			return False
	return True

# Multiplies all numbers in the array
def mult(numbers):
	return reduce(lambda x, y: x * y, numbers)

# Returns a list of all primes less than the limit
def sieve(limit):
	isPrime = [True for i in range(limit + 1)]
	primes = []
	p = 2
	while p * p <= limit:
		if isPrime[p]:
			for i in range(p * 2, limit + 1, p):
				isPrime[i] = False
		p += 1
	for i in range(2, len(isPrime)):
		if isPrime[i]:
			primes.append(i)
	return primes

# Determines if the number is reversible as per the Project Euler definition
def is_reversible(number):
	number = str(number + int(str(number)[::-1]))
	for char in number:
		if int(char) % 2 == 0:
			return False
	return True

# Determines the number of divisors in a number
def num_divisors(number):
	num_divs = 0
	for i in range(1, int(sqrt(number)) + 1):
		if number % i == 0:
			num_divs += 2
	if(sqrt(number) * sqrt(number) == float(number)):
		num_divs -= 1
	return num_divs

# Returns the product of n consecutive numbers in a grid in a given direction
def grid_product(grid, x, y, xdir, ydir, limit):
	return mult(grid[y + i * ydir][x + i * xdir] for i in range(limit))

# Determines the length of a collatz chain
@memorize
def collatz_chain(x):
	if x == 1:
		return 1
	elif x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatz_chain(y) + 1

# Returns a list of proper divisors of a given number
def proper_divisors(number):
	divisors = []
	if number <= 1:
		return divisors
	for i in range(1, number):
		if number % i == 0:
			divisors.append(i)
	return divisors

# Determines if the input is pandigital on the given size
def is_pandigital(number):
	digits = list(map(int, str(number)))
	if digits[0] == 0:
		return False
	digits.sort()
	return digits == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

import datetime
import fractions
from functools import reduce
from itertools import count,filterfalse,islice,permutations
from math import *
import os
import platform
import roman
import sys

system = platform.system()

# +----------------+
# | Engine Library |
# +----------------+

# Clears the terminal screen
def clear():
	if system in ['Darwin', 'Linux']:
		os.system('clear')
	elif system in ['Windows']:
		os.system('cls')
	else:
		print('An error occured clearing the screen. OS and/or Terminal Session not supported')
	return None

# Formats a timestamp into a more readable format
def format_time(timeElapsed):
	if timeElapsed < 0.000001:
		timeElapsed *= 1000000000
		return '{0:.3f} ns'.format(timeElapsed)
	elif timeElapsed < 0.001:
		timeElapsed *= 1000000
		return '{0:.3f} \u03BCs'.format(timeElapsed)
	elif timeElapsed < 1:
		timeElapsed *= 1000
		return '{0:.3f} ms'.format(timeElapsed)
	elif timeElapsed < 60:
		return '{0:.3f} sec'.format(timeElapsed)
	else:
		mins = int(timeElapsed // 60)
		timeElapsed -= (60 * mins)
		return '{0} mins {1:.3f} sec'.format(mins, timeElapsed)

# Reports a number in a readable format
def report(ans):
	if isinstance(ans, int):
		print('Answer: {0:,}'.format(ans))
	elif isinstance(ans, float):
		print('Answer: {0:,.10f}'.format(ans))
	else:
		print('Answer: {0}'.format(ans))
	return None

# +-------------------+
# | Challenge Library |
# +-------------------+

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

# Determines if a string is a palindrome
def is_palindrome(num):
	return str(num) == str(num)[::-1]

# Determines if a number is evenly divisible by all numbers in the given range
def is_smallest_multiple(num, rng):
	for i in range(rng, 2, -1):
		if num % i != 0:
			return False
	return True

# Determines if a number is prime
def is_prime(num):
	if num == 2:
		return True
	elif num % 2 == 0 or num < 2:
		return False
	i = 3
	while i**2 <= num:
		if num % i == 0:
			return False
		else:
			i += 2
	return True

# Multiplies a list of numbers together into one product
def mult(nums):
	return reduce((lambda x, y: x * y), nums)

# Generates a list of primes using the Sieve of Eratosthenes algorithm
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

# Determines the number of divisors of a given number
def num_divisors(number):
	count = 1
	i = 2
	while i * i <= number:
		if number % i == 0:
			count += 2
		i += 1
	if int(sqrt(number) * sqrt(number)) == number:
		count -= 1
	return count

# Determines the length of a collatz chain with a given starting number
@memorize
def collatz_chain(x):
	if x == 1:
		return 1
	elif x % 2 == 0:
		y = x // 2
	else:
		y = x * 3 + 1
	return collatz_chain(y) + 1

# Converts a number from digit to word form
def num_to_word(num):
	units = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
	tens = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()
	word = ''
	if num // 1000 > 0:
		word += units[num // 1000] + ' thousand '
		num %= 1000
	if num // 100 > 0:
		word += units[num // 100] + ' hundred'
		num %= 100
		if num > 0:
			word += ' and '
	if num >= 20:
		word += tens[num // 10] + ' '
		num %= 10
	if num > 0:
		word += units[num]
	return word

# Returns the proper divisors of a number
def proper_divisors(num):
	divs = []
	for i in range(1, num):
		if num % i == 0:
			divs.append(i)
	return divs

# Determines if a number is pandigital
def is_pandigital(num):
	check = '123456789'
	temp = ''.join(map(str, sorted(list(map(int, str(num))))))
	return temp == check[:len(temp)]

# Determines if two strings are permutations of each other
def is_perm(a, b):
	return sorted(str(a)) == sorted(str(b))

roman_values = [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40), ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)]

# Converts a roman numeral into an arabic numeral
def to_arabic(roman):
	arabic = 0
	while len(roman) > 0:
		for (pre, val) in roman_values:
			if roman.startswith(pre):
				arabic += val
				roman = roman[len(pre):]
	return arabic

# Converts an arabic numeral into a roman numeral
def to_roman(arabic):
	if arabic == 0:
		return ''
	for (pre, val) in roman_values:
		if arabic >= val:
			arabic -= val
			return pre + to_roman(arabic)

if __name__ == '__main__':
	clear()
	print('Library cannot be invoked directly!')

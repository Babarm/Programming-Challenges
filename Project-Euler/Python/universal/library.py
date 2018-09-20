import datetime
import fractions
from functools import reduce
from itertools import count, filterfalse, islice, permutations
from math import *
import os
import platform
from primesieve import *
import sys

if __name__ == '__main__':
	print('Please start program via main.py')

class memoize(object):
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

def is_palindrome(val):
	return str(val) == str(val)[::-1]

def is_smallest_multiple(val, limit):
	for i in range(limit, 1, -1):
		if val % i != 0:
			return False
	return True

def is_prime(val):
	if val == 2: 
		return True
	elif val % 2 == 0 or val < 2:
		return False
	i = 3
	while i**2 <= val:
		if val % i == 0:
			return False
		else:
			i+= 2
	return True

def mult(nums):
	return reduce((lambda x, y: x * y), nums)

def num_divisors(val):
	count = 1
	i = 2
	while i * i <= val:
		if val % i == 0:
			count += 2
		i += 1
	if int(sqrt(val) * sqrt(val)) == val:
		count -= 1
	return count

@memoize
def collatz(n):
	if n < 1:
		return 0
	if n == 1:
		return 1
	if n % 2 == 0:
		m = n // 2
	else:
		m = 3 * n + 1
	return collatz(m) + 1

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

def proper_divisors(num):
	divs = []
	for i in range(1, num):
		if num % i == 0:
			divs.append(i)
	return divs

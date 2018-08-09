from math import *

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
	if number % 2 == 0 and number > 2:
		return False
	return all(number % i for i in range(3, int(sqrt(number)) + 1, 2))

# Multiplies all numbers in the array
def mult(numbers):
	result = 1
	for number in numbers:
		result *= number
	return result

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

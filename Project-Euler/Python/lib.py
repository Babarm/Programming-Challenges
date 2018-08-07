import time
import os
import sys
import platform
from math import *

if platform.system() in ['Windows']:
	import msvcrt
	import ctypes
	class _CursorInfo(ctyps.Structure):
		_fields_ = [("size", ctypes.c_int),
					("visible", ctypes.c_byte)]

# Clears the screen to make it easier to see what's happening
def clear():
	sys = platform.system()
	if sys in ['Darwin', 'Linux']:
		os.system('clear')
	elif sys in ['Windows']:
		os.system('cls')
	return None

# Formats time elapsed into a more readable format
def formatTime(timeElapsed):
	formattedTime = None
	if timeElapsed < 1:
		formattedTime = '{0:,.3f} ms'.format(timeElapsed * 1000)
	else:
		formattedTime = '{0:,.3f} sec'.format(timeElapsed)
	return formattedTime

# Hides the cursor
def hide_cursor():
	if platform.system() in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = False
		ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
	elif platform.system() in ['Darwin', 'Linux']:
		sys.stdout.write("\033[?25l")
		sys.stdout.flush()

# Shows the cursor
def show_cursor():
	if platform.system() in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = True
		ctypes.windll.kernel32.SerConsoleCursorInfo(handle, ctypes.byref(ci))
	elif platform.system() in ['Darwin', 'Linux']:
		sys.stdout.write("\033[?25h")
		sys.stdout.flush()

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

from lib import *

clear()
print('Question 24')
print('Level 1\n')
print('Python has many built-in functions, and if you do not know how to use it,')
print('you can read document online or find some books. Please write a program')
print('to print some Python built-in functions documents, such as abs(), int()')
print('And add document for your own function\n\n')

def square(n):
	'''This is the documentation of the method 'square()'.
	Input must be an integer.
	'''

	return n**2

print(square.__doc__)
print(square(2))

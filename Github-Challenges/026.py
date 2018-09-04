from lib import *

clear()
print('Question 26')
print('Level N/A\n')
print('Define a function that can compute the sum of two numbers\n\n')

def sum(a, b):
	return a + b

a, b = map(int, input('Please enter two numbers: ').split())

print('{0:,}'.format(sum(a, b)))

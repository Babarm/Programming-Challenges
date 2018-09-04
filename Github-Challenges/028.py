from lib import *

clear()

print('Question 28')
print('Level N/A\n')
print('Define a function that can receive two integral numbers in string form and print to console.\n\n')

def sum(a, b):
	return int(a) + int(b)

a, b = input('Please enter two numbers: ').split()

print(sum(a, b))

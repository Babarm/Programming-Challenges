from lib import *

clear()

def int_to_str(num):
	return '{0:,}'.format(num)

print('Question 27')
print('Level N/A\n')
print('Define a function that can convert an integer into a string and print it in console.\n\n')

number = int(input('Please enter a number: '))

print(int_to_str(number))

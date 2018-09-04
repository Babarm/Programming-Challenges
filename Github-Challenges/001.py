from lib import *

clear()
print('Question 1')
print('Level 1\n')
print('Write a program which will find all such numbers which are divisible by')
print('7 but are not a multiple of 5 between 2,000 and 3,200 (inclusive).')
print('The numbers obtained should be printed in a comma-separated sequence on a')
print('single line.\n\n')

numbers = []

for i in range(2000, 3201):
	if i % 7 == 0 and i % 5 != 0:
		numbers.append(i)

print(numbers)

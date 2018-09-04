from lib import *

clear()
print('Question 12')
print('Level 2\n')
print('Write a program, which will find all such numbers between 1000 and 3000')
print('(inclusive) such that each digit of the number is an even number.')
print('The numbers obtained should be printed in a comma-separated sequence')
print('on a single line\n\n')

valids = []

for i in range(1000, 3001):
	valid = True
	for digit in list(map(int, str(i))):
		if digit % 2 != 0:
			valid = False
	if valid:
		valids.append(str(i))

print(','.join(valids))

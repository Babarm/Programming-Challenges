from lib import *

clear()
from math import floor,sqrt

print('Question 6')
print('Level 2\n')
print('Write a program that calculates and prints the value according to the')
print('given formula:')
print('Q = \u221A((2 * C * D) / H)')
print('C = 50')
print('H = 30')
print('D is the variable whose value should be input to the program in a comma-')
print('separated sequence.\n')
print('Example:')
print('Let us assume the following comma-separated input sequence is given to')
print('the program:')
print('100,150,180')
print('The output of the program should be:')
print('18,22,24\n\n')

Ds = list(map(int, input('Enter some numbers separated by commas: ').replace(' ', '').split(',')))
results = []
for D in Ds:
	results.append(int(floor(sqrt((2 * 50 * D) / 30))))
results = list(map(str, results))
print(','.join(results))

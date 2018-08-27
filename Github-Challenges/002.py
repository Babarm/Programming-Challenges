import sys

print('Question 2')
print('Level 1\n')
print('Write a program which can compute the factorial of a given number.')
print('The results should be printed in a comma-separated sequence on a single')
print('line.\n')
print('Suppose the following input is supplied to the program:')
print('8')
print('Then, the output should be:')
print('40,320\n\n')

sys.setrecursionlimit(100000)

def factorial(num):
	if num == 0:
		return 1
	else:
		return num * factorial(num - 1)


num = int(input('Please enter a number: '))
print('{0:,}'.format(factorial(num)))

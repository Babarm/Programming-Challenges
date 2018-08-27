print('Question 14')
print('Level 2\n')
print('Write a program that accepts a sentence and calculates the number of')
print('upper case and lower case letters.')
print('Suppose the following input is supplied to the program:')
print('Hello world!')
print('The output should be:')
print('UPPER CASE: 1')
print('LOWER CASE: 9\n\n')

string = input('Please enter some text: ')

upper = 0
lower = 0

for char in string:
	upper += 1 if char.isupper() else 0
	lower += 1 if char.islower() else 0

print('UPPER CASE: {0}'.format(upper))
print('LOWER CASE: {0}'.format(lower))

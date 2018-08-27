print('Question 11')
print('Level 2\n')
print('Write a program that accepts a sequence of comma separated 4 digit binary')
print('numbers as its input and then check whether they are divisible by 5 or')
print('not. The numbers that are divisible by 5 are to be printed in a comma')
print('separated sequence\n')
print('Example:')
print('0100,0011,1010,1001')
print('Output:')
print('1010')
print('Note: Assume the data is input by console\n\n')

inputs = input('Please enter the numbers: ').replace(' ', '').split(',')

valids = []

for i in inputs:
	if int(i, 2) % 5 == 0:
		valids.append(i)

print(','.join(valids))

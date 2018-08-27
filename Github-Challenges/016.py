print('Question 16')
print('Level 2\n')
print('Use a list comprehension to square each odd number in a list. The list is')
print('input by a sequence of comma-separated numbers.')
print('Suppose the following input is supplied to the program:')
print('1,2,3,4,5,6,7,8,9')
print('The output should be:')
print('1,9,25,49,81\n\n')

numbers = list(map(int, input('Please enter some numbers: ').replace(' ', '').split(',')))

results = []

for number in numbers:
	if number % 2 != 0:
		results.append(number * number)

print(','.join(list(map(str, results))))

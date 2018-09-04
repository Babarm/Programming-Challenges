from lib import *

clear()
print('Question 3')
print('Level 1\n')
print('With a given integral number n, write a program to generate a dictionary')
print('that contains (i, i * i) such that is an integral number between 1 and n')
print('(inclusive) and then the program should print the dictionary.\n')
print('Suppose the following input is supplied to the program:')
print('8')
print('Then, the output should be:')
print('{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}\n\n')

limit = int(input('Please enter a number: '))

dictionary = {}

for i in range(1, limit + 1):
	dictionary[i] = i * i

print(dictionary)

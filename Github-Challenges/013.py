from lib import *

clear()
print('Question 13')
print('Level 2\n')
print('Write a program that accepts a sentence and calculate the number of')
print('letters and digits.')
print('Suppose the following input is supplied to the program:')
print('hello world! 123')
print('The output should be:')
print('LETTERS 10')
print('DIGITS 3\n\n')

string = input('Please enter some text: ').upper()

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
		   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

numLetters = 0
numDigits = 0

for char in string:
	numLetters += 1 if char.isalpha() else 0
	numDigits += 1 if char.isdigit() else 0

print('LETTERS: {0}'.format(numLetters))
print('DIGITS:  {0}'.format(numDigits))

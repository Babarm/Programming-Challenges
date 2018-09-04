from lib import *

clear()
print('Question 9')
print('Level 2\n')
print('Write a program that accepts a sequence of lines as input and prints the')
print('lines after making all characters in the sentence capitalized.')
print('Suppose the following input is supplied to the program:')
print('Hello world')
print('Practice makes perfect')
print('Then the output should be:')
print('HELLO WORLD')
print('PRACTICE MAKES PERFECT\n\n')

sentences = []

sentence = ''

print('Enter some sentences [BLANK line to continue]:')

while True:
	sentence = input().upper()
	if sentence == '':
		break
	sentences.append(sentence)

for string in sentences:
	print(string)

from lib import *

clear()

print('Question 29')
print('Level N/A\n')
print('Define a function that can accept two strings as input and concatenate them and print to console\n\n')

def concat(str1, str2):
	return str(str1) + str(str2)

text = []

while True:
	line = input('')
	if not line:
		break
	text.append(line)

while len(text) > 1:
	text[len(text) - 2] = concat(text[len(text) - 2], text[len(text) - 1])
	text.pop(len(text) - 1)

print(text[0])

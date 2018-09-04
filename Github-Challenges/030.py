from lib import *

clear()

print('Question 30')
print('Level N/A\n')
print('Define a function that can accept two strings as input and print the string with the maximum length to the console')

lines = []

while True:
	line = input('')
	if not line:
		break
	lines.append(line)

biggest = 0
bigs = []

for line in lines:
	if len(line) > biggest:
		bigs = []
		bigs.append(line)
		biggest = len(line)
	elif len(line) == biggest:
		bigs.append(line)


for line in bigs:
	print(line)

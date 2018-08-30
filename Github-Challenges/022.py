print('Question 22')
print('Level 3\n')
print('Write a program to compute the frequency of the words from the input. The')
print('output should be sorted alphanumerically.')
print('Suppose the following input is supplied to the program:')
print("'New to Python or choosing between Python 2 and Python 3? Read Python 2 or Python 3.'")
print('Then the output should be:')
print('2:2')
print('3?:1')
print('3.:1')
print('New:1')
print('Python:5')
print('Read:1')
print('and:')
print('between:1')
print('choosing:1')
print('or:2')
print('to:1\n\n')

from operator import itemgetter

frequency = {}

string = list(input('Please enter some text: ').split(' '))
for word in string:
	if word in frequency:
		frequency[word] += 1
	else:
		frequency[word] = 1

frequency = sorted(frequency, key=itemgetter(0))

print(frequency)

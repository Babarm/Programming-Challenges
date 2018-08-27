print('Question 17')
print('Level 2\n')
print('Write a program that computes the net amount of a bank account based on')
print('a transaction log from console input. The transaction log format is shown')
print('as following:')
print('D 100')
print('W 200\n')
print('D means deposit while W means withdrawl')
print('Suppose the following input is supplied to the program')
print('D 300')
print('D 300')
print('W 200')
print('D 100')
print('Then, the output should be:')
print('500\n\n')

commands = []

while True:
	command = input()
	if command:
		commands.append(command.upper())
	else:
		break

balance = 0

for string in commands:
	string.replace(' ', '')
	if string[0] not in ['D', 'W']:
		continue
	else:
		if string[0] == 'D':
			balance += int(string[1:])
		else:
			balance -= int(string[1:])

print(balance)

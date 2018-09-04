from lib import *

clear()
print('Question 18')
print('Level 3\n')
print('A website requires the users to input username and password to register')
print('Write a program to check the validity of password input by users.')
print('Following are the criteria for checking the password:')
print('1. At least 1 letter between [a-z]')
print('2. At least 1 number between [0-9]')
print('3. At least 1 letter between [A-Z]')
print('4. At least 1 character from [$#@]')
print('5. Minimum length of transaction password: 6')
print('6. Maximum length of transaction password: 12')
print('Your programm should accept a sequence of comma separated passwords')
print('and will check them according to the above criteria. Passwords that match')
print('the criteria are to be printed, each separated by a comma.')
print('Example:')
print('If the following passwords are given as input to the program:')
print('ABd1234@1,a F1#, 2w3E*, 2We3345')
print('The output should be:')
print('ABd1234@1\n\n')

passwords = input('Please enter the passwords: ').split(',')

valids = []

for password in passwords:
	valid = True
	hasUpper = hasLower = hasDigit = hasSpecial = False
	if len(password) < 6 or len(password) > 12:
		continue
	for char in password:
		if char.isupper():
			hasUpper = True
		if char.islower():
			hasLower = True
		if char.isdigit():
			hasDigit = True
		if char in '$#@':
			hasSpecial = True
	if not hasUpper or not hasLower or not hasDigit or not hasSpecial:
		valid = False
	if valid:
		valids.append(password)


print(','.join(valids))

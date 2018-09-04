from lib import *

clear()
print('Question 15')
print('Level 2\n')
print('Write a program that computes the vlaue of a + aa + aaa + aaaa with a')
print('given digit as the value of a.')
print('Suppose the following input is supplied to the program:')
print('9')
print('The output should be:')
print('11106\n\n')

num = int(input('Please enter a number: '))

ans = num + int('{0}{0}'.format(num)) + int('{0}{0}{0}'.format(num)) + int('{0}{0}{0}{0}'.format(num))

print(ans)

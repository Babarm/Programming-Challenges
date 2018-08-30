print('Question 23')
print('Level 1\n')
print('Write a method to calculate the square value of a number\n\n')

def square(n):
	return n**2

n = int(input('Please enter a number: '))
print('Square: {0:,}'.format(square(n)))

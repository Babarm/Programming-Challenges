print('Question 20')
print('Level 3\n')
print('Define a class with a generator which can iterate the numbers, which are')
print('divisible by 7, between a given range 0 and n.\n\n')

def gen(n):
	i = 0
	while i < n:
		j = i
		i += 1
		if j % 7 == 0:
			yield str(j)

n = int(input('Please enter a number: '))

print(','.join(gen(n)))

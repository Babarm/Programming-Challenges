print('Question 7')
print('Level 2\n')
print('Write a program that takes 2 digits, X and Y, as input and generates a')
print('2-Dimensional array. The element value in the i-th row and j-th column')
print('should be i * j.\n')
print('Note: i=0,1,...,X-1; j=0,1,...Y-1\n')
print('Example:')
print('Suppose the following inputs are given to the program:')
print('3,5')
print('The output of the program should be:')
print('[[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]\n\n')

X, Y = map(int, input('Enter the array dimensions: ').replace(' ', '').split(','))

array = [[0 for y in range(Y)] for x in range(X)]

for x in range(X):
	for y in range(Y):
		array[x][y] = x * y

print(array)

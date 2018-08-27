print('Question 8')
print('Level 2\n')
print('Write a program that accepts a comma separated sequence of words as input')
print('and prints the words in a comma separated sequence after sorting them')
print('alphabetically.\n')
print('Suppose the following input is supplied to the program:')
print('without,hello,bag,world')
print('The output of the program should be:')
print('bag,hello,without,world\n')

words = sorted(list(input('Please enter some words: ').replace(' ', '').split(',')))

print(','.join(words))

from lib import *

clear()
print('Question 10')
print('Level 2\n')
print('Write a program that accepts a sequence of whitespace separated words as')
print('input and prints the words after removing all duplicate words and sorting')
print('them alphanumerically.\n')
print('Suppose the following input is supplied to the program:')
print('hello world and practice makes perfect and hello world again')
print('The output of the program should be:')
print('again and hello makes perfect practice world\n\n')

words = sorted(list(set(input('Please enter some words: ').split(' '))))
print(' '.join(words))

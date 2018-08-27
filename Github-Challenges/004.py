print('Question 4')
print('Level 1\n')
print('Write a program which accepts a sequence of comma-separated numbers from')
print('console and generate a list and a tuple which contains every number.\n')
print('Suppose the following input is supplied to the program:')
print('34,67,55,33,12,98')
print('Then, the output should be:')
print("['34', '67', '55', '33', '12', '98']")
print("('34', '67', '55', '33', '12', '98')\n\n")

nums = input('Please enter some numbers separated by commas: ').replace(' ', '').split(',')

list_nums = list(nums)
tuple_nums = tuple(nums)

print(list_nums)
print(tuple_nums)

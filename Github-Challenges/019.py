print('Question 19')
print('Level 3\n')
print('You are required to write a program to sort the (name, age, height) tuples')
print('by ascending order where name is string, age and height are numbers. The')
print('tuples are input by console. The sort criteria is:')
print('1: Sort based on name')
print('2: Then sort based on age')
print('3: Then sort by score')
print('The priority is that name > age > score')
print('If the following inputs are given to the program:')
print('Tom,19,80')
print('John,20,90')
print('Jony,17,91')
print('Jony,17,93')
print('Json,21,85')
print('Then the output should be:')
print("[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]\n\n")

from operator import itemgetter

students = []

while True:
	s = input()
	if s:
		students.append(tuple(s.replace(' ', '').split(',')))
	else:
		break

students = sorted(students, key = itemgetter(0, 1, 2))

print(students)

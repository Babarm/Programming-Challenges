from lib import *

clear()
print('Question 21')
print('Level 3\n')
print('A robot moves in a plane starting from the original point (0,0). The robot')
print('can move UP, DOWN, LEFT, and RIGHT with a given steps. The trace of robot')
print('movement is shown as the following:')
print('UP 5')
print('DOWN 3')
print('LEFT 3')
print('RIGHT 2')
print('The numbers after the direction are steps. Please write a program to')
print('compute the distance from current position after a sequence of movement')
print('and original point. If the distance is a float, then just print the')
print('nearest integer.\n')
print('Example:')
print('If the following tuples are given as input to the program:')
print('UP 5')
print('DOWN 3')
print('LEFT 3')
print('RIGHT 2')
print('Then the output should be:')
print('2\n\n')

from math import hypot

origin = [0,0]
place = origin

while True:
	move = input('').upper()
	if move:
		command = move.split(' ')
		if command[0] == 'UP':
			place[1] += int(command[1])
		elif command[0] == 'DOWN':
			place[1] -= int(command[1])
		elif command[0] == 'RIGHT':
			place[0] += int(command[1])
		elif command[0] == 'LEFT':
			place[0] -= int(command[1])
		else:
			pass
	else:
		break

print('Distance from origin: {0:,}'.format(round(hypot(place[0] - 0, place[1] - 0))))

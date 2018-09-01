from lib import *
import time

triangle = []

def run():
	with open('data/018.txt', 'r') as f:
		for line in f:
			triangle.append(list(map(int, line.strip().split())))
	for i in range(len(triangle) - 2, -1, -1):
		for j in range(len(triangle[i])):
			triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])
	return triangle[0][0]

clear()

print('Challenge #18: Maximum Path Sum I')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

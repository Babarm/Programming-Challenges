from lib import *
import time

def run():
	ans = 0
	t = 286
	p = 166
	h = 144
	while True:
		triangle = t * (t + 1) // 2
		pentagon = p * (3 * p - 1) // 2
		hexagon = h * (2 * h - 1)
		minimum = min(triangle, pentagon, hexagon)
		if minimum == max(triangle, pentagon, hexagon):
			ans = triangle
			break
		t += 1 if minimum == triangle else 0
		p += 1 if minimum == pentagon else 0
		h += 1 if minimum == hexagon else 0
	return ans

clear()

print('Challenge #45: Triangular, Pentagonal, and Hexagonal')
print('====================================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

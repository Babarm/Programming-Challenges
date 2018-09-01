from lib import *
import time

def run():
	ans = 0
	for a in range(500):
		for b in range(333):
			c = 1000 - a - b
			if a * a + b * b == c * c:
				ans = a * b * c
	return ans

clear()

print('Challenge #9: Special Pythagorean Triplet')
print('=========================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

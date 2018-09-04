from lib import *
import time

def count_sols(p):
	result = 0
	for a in range(1, p + 1):
		for b in range(a, (p - a) // 2 + 1):
			c = p - a - b
			if a * a + b * b == c * c:
				result += 1
	return result

def run():
	ans = max(range(1, 1001), key=count_sols)
	return ans

clear()

print('Challenge #39: Integer Right Triangles')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

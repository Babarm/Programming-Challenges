from lib import *
import time

def run():
	return max(range(1, 1000), key=cycle_len)

def cycle_len(n):
	seen = {}
	x = 1
	for i in count():
		if x in seen:
			return i - seen[x]
		else:
			seen[x] = i
			x = x * 10 % n

clear()

print('Challenge #26: Reciprocal Cycles')
print('================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

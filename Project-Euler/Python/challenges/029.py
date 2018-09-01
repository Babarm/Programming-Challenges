from lib import *
import time

def run():
	seen = []
	for a in range(2, 101):
		for b in range(2, 101):
			if a**b not in seen:
				seen.append(a**b)
	seen = set(seen)
	return len(seen)

clear()

print('Challenge #29: Distinct Powers')
print('==============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

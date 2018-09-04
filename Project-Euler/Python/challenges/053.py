from lib import *
import time

def c(n, r):
	return factorial(n) // (factorial(r) * factorial(n - r))

def run():
	return sum(1 for n in range(1, 101) for r in range(1, n + 1) if c(n, r) > 1000000)

clear()

print('Challenge #53: Combinatoric Selections')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

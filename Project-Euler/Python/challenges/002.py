from lib import *
import time

def run():
	ans = a = 0
	b = fib = 1
	while fib < 4000000:
		fib = a + b
		a = b
		b = fib
		if fib % 2 == 0:
			ans += fib
	return ans

clear()

print('Challenge #2: Even Fibonacci Numbers')
print('====================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

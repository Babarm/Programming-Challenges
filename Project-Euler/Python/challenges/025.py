from lib import *
import time

def run():
	ans = 1
	a = 0
	b = fib = 1
	while True:
		fib = a + b
		a = b
		b = fib
		ans += 1
		if len(str(fib)) >= 1000:
			break
	return ans

clear()

print('Challenge #25: 1000-digit Fibonacci Number')
print('==========================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

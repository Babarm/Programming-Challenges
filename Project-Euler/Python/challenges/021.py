from lib import *
import time

def run():
	ans = 0
	for a in range(10000):
		b = sum(proper_divisors(a))
		if a == sum(proper_divisors(b)) and a != b:
			ans += a
	return ans

clear()

print('Challenge #21: Amicable Numbers')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	ans = 0
	i = 1
	count = 0
	while count < 500:
		ans += i
		count = num_divisors(ans)
		i += 1
	return ans

clear()

print('Challenge #12: Highly Divisible Triangular Number')
print('=================================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

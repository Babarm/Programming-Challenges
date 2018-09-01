from lib import *
import time

def run():
	ans = 1
	count = 1
	while count < 10001:
		ans += 2
		if is_prime(ans):
			count += 1
	return ans

clear()

print('Challenge #7: 10 001st Prime')
print('============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

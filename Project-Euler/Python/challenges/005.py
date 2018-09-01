from lib import *
import time

def run():
	ans = 80
	while True:
		if is_smallest_multiple(ans, 20):
			break
		ans += 80
	return ans

clear()

print('Challenge #5: Smallest Multiple')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

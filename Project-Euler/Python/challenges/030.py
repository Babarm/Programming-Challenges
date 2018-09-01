from lib import *
import time

def run():
	ans = 0
	limit = 450000
	for i in range(2, 450000):
		if sum(j**5 for j in map(int, str(i))) == i:
			ans += i
	return ans

clear()

print('Challenge #30: Digit Fifth Powers')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

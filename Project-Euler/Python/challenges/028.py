from lib import *
import time

def run():
	ans = 1
	for i in range(1, 501):
		square = (2 * i + 1)**2
		ans += square + (square - (2 * i)) + (square - (4 * i)) + (square - (6 * i))
	return ans

clear()

print('Challenge #28: Number Spiral Diagonals')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	ans = 0
	ans = max(sum(map(int, str(a**b))) for a in range(100) for b in range(100))
	return ans

clear()

print('Challenge #56: Powerful Digit Sum')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

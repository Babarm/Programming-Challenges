from lib import *
import time

def run():
	ans = 0
	numer = 0
	denom = 1
	for i in range(1000):
		numer, denom = denom, denom * 2 + numer
		if len(str(numer + denom)) > len(str(denom)):
			ans += 1
	return ans

clear()

print('Challenge #57: Square Root Convergents')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

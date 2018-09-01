from lib import *
import time

def run():
	return sum(i for i in range(101)) * sum(i for i in range(101)) - sum(i * i for i in range(101))
clear()

print('Challenge #6: Sum Square Difference')
print('===================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

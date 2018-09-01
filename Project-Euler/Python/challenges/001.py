from lib import *
import time

def run():
	return sum(i for i in range(1000) if i % 3 == 0 or i % 5 ==0)

clear()

print('Challenge #1: Multiple of 3 and 5')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

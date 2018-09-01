from lib import *
import time

def run():
	return sum(map(int, str(2**1000)))

clear()

print('Challenge #16: Power Digit Sum')
print('==============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

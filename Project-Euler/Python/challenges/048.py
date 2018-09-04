from lib import *
import time

def run():
	return int(str(sum(i**i for i in range(1, 1000)))[-10:])

clear()

print('Challenge #48: Self Powers')
print('==========================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

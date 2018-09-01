from lib import *
import time

def run():
	return sum(1 for i in range(1901, 2001) for j in range(1, 13) if datetime.date(i, j, 1).weekday() == 6)

clear()

print('Challenge #19: Counting Sundays')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

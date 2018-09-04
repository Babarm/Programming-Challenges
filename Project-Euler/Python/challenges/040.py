from lib import *
import time

def run():
	index = 1
	constant = ' '
	while len(constant) < 1000001:
		constant += str(index)
		index += 1
	ans = int(constant[1]) * int(constant[10]) * int(constant[100]) * int(constant[1000]) * int(constant[10000]) * int(constant[100000]) * int(constant[1000000])
	return ans

clear()

print('Challenge #40: Champernowne\'s Constant')
print('=======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

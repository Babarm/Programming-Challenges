from lib import *
import time

def run():
	return sum(len(num_to_word(i).replace(' ','')) for i in range(1, 1001))

clear()

print('Challenge #17: Number Letter Counts')
print('===================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	return factorial(40) // (factorial(20) * factorial(20))

clear()

print('Challenge #15: Lattice Paths')
print('============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

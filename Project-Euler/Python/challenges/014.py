from lib import *
import sys
import time

sys.setrecursionlimit(3000)

def run():
	return max(range(1,1000000), key=collatz_chain)

clear()

print('Challenge #14: Longest Collatz Sequence')
print('=======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	ans = 0
	with open('data/013.txt', 'r') as f:
		ans = str(sum(int(num) for num in f))[:10]
	return ans

clear()

print('Challenge #13: Large Sum')
print('========================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

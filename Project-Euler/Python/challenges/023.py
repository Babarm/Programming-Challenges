from lib import *
import time

def run():
	ans = 0
	limit = 28124
	sums = [0] * limit
	for i in range(1, limit):
		for j in range(i * 2, limit, i):
			sums[j] += i
	abundants = [i for (i, x) in enumerate(sums) if x > i]
	expressable = [False] * limit
	for i in abundants:
		for j in abundants:
			if i + j < limit:
				expressable[i + j] = True
			else:
				break
	ans = sum(i for (i, x) in enumerate(expressable) if not x)
	return ans

clear()

print('Challenge #23: Non-Abundant Sums')
print('================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

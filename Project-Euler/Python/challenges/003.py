from lib import *
import time

def run():
	ans = 0
	limit = 600851475143
	i = 2
	while i * i < limit:
		if limit % i == 0:
			limit /= i
			ans = i
		else:
			i += 1
	if limit > ans:
		ans = limit
	return int(ans)

clear()

print('Challenge #: Largest Prime Factor')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

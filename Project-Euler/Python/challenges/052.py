from lib import *
import time

def run():
	ans = 0
	i = 1
	while True:
		a = i * 2
		b = i * 3
		c = i * 4
		d = i * 5
		e = i * 6
		if all(is_perm(i, j) for j in [a, b, c, d, e]):
			ans = i
			break
		i += 2
	return ans

clear()

print('Challenge #52: Permuted Multiples')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

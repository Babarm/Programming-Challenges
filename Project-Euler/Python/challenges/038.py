from lib import *
import time

def run():
	ans = 0
	for i in range(1, 10000):
		pandigital = ''
		n = 1
		while len(pandigital) < 9:
			pandigital += str(i * n)
			n += 1
		if is_pandigital(pandigital) and int(pandigital) > ans:
			ans = int(pandigital)
	return ans

clear()

print('Challenge #38: Pandigital Multiples')
print('===================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

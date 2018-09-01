from lib import *
import time

def run():
	ans = 0
	prods = []
	for a in range(10):
		for b in range(1000, 10000):
			c = a * b
			if ''.join(sorted(str(a) + str(b) + str(c))) == '123456789':
				prods.append(c)
	for a in range(10, 100):
		for b in range(100, 1000):
			c = a * b
			if ''.join(sorted(str(a) + str(b) + str(c))) == '123456789':
				prods.append(c)
	prods = set(prods)
	ans = sum(prods)
	return ans

clear()

print('Challenge #32: Pandigital Products')
print('==================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

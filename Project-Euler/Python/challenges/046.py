from lib import *
import time

def test(num):
	if num % 2 == 0 or is_prime(num):
		return True
	for i in count(1):
		k = num - 2 * i * i
		if k <= 0:
			return False
		elif is_prime(k):
			return True

def run():
	return next(filterfalse(test, count(9, 2)))

clear()

print('Challenge #46: Goldbach\'s Other Conjecture')
print('==========================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	ans = 0
	primes = reversed(sieve(7654321))
	for prime in primes:
		if is_pandigital(prime):
			ans = prime
			break
	return ans

clear()

print('Challenge #41: Pandigital Prime')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

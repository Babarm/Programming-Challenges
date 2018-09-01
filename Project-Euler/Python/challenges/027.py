from lib import *
import time

def run():
	ans = 0
	max_primes = 0
	for a in range(-999, 1000):
		for b in range(-1000, 1001):
			n = 0
			while is_prime(n * n + a * n + b):
				n += 1
			if n > max_primes:
				max_primes = n
				ans = a * b
	return ans

clear()

print('Challenge #27: Quadratic Primes')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

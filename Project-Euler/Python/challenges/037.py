from lib import *
import time

def is_truncatable(n):
	i = 10
	while i <= n:
		if not is_prime(n % i):
			return False
		i *= 10
	while n > 0:
		if not is_prime(n):
			return False
		n //= 10
	return True

def run():
	ans = 0
	prime = 11
	i = 0
	while i < 11:
		if is_truncatable(prime):
			ans += prime
			i += 1
		prime += 2
	return ans

clear()

print('Challenge #37: Truncatable Primes')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

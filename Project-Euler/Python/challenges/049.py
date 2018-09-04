from lib import *
import time

def run():
	ans = 0
	limit = 10000
	primes = sieve(limit)
	for base in primes:
		if base == 1487: continue
		a = base + 3330
		b = a + 3330
		nums = [a, b]
		if all(k in primes for k in nums) and all(is_perm(k, base) for k in nums):
			ans = int(str(base) + str(a) + str(b))
			break
	return ans

clear()

print('Challenge #49: Prime Permutations')
print('=================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

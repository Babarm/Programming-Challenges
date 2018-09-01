from lib import *
import time

def run():
	return sum(sieve(2000000))

clear()

print('Challenge #10: Summation of Primes')
print('==================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

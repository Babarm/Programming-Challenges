from lib import *
import time

def rotate(prime):
	return int(str(prime)[1:] + str(prime)[0])

def run():
	ans = 0
	primes = sieve(1000000)
	for i, prime in enumerate(primes):
		if any(digit in str(prime) for digit in ['0', '2', '4', '5', '6', '8']) and prime not in [2, 5]:
			continue
		new_prime = rotate(prime)
		is_circ = True
		while new_prime != prime:
			if new_prime not in primes:
				is_circ = False
			new_prime = rotate(new_prime)
		if is_circ:
			ans += 1
	return ans

clear()

print('Challenge #35: Circular Primes')
print('==============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

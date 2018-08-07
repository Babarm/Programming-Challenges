from lib import *

def phi(n):
	result = 0
	for i in range(1, n):
		if gcd(i, n) == 1:
			result += 1
	return result

def is_permutation(a, b):
	a = str(a)
	a = ''.join(sorted(a))
	b = str(b)
	b = ''.join(sorted(b))
	return a == b

clear()

hide_cursor()

print('Challenge #: \n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

print(phi(10000000))

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

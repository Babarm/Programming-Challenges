from lib import *

clear()

hide_cursor()

print('Challenge #7: 10 001st Prime\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

ans = 3
numPrimes = 1
while True:
	if is_prime(ans):
		numPrimes += 1
		if numPrimes == 10001:
			break
	ans += 2

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

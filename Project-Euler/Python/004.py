from lib import *

clear()

hide_cursor()

print('Challenge #4: Largest Palindrome Product\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

for a in range(100, 1000):
	for b in range(100, 1000):
		c = a * b
		if is_palindrome(c) and ans < c:
			ans = c

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

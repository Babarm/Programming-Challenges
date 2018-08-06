from lib import *

clear()

hide_cursor()

print('Challenge #9: Special Pythagorean Triplet\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

for a in range(500):
	for b in range(333):
		c = 1000 - a - b
		if a * a + b * b == c * c:
			ans = a * b * c

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

from lib import *

clear()

hide_cursor()

print('Challenge #1: Multiples of 3 and 5\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

for i in range(1000):
	ans += i if i % 3 == 0 or i % 5 == 0 else 0

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

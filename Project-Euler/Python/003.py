from lib import *

clear()

hide_cursor()

print('Challenge #3: Largest Prime Factor\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

limit = 600851475143

for i in range(1, int(sqrt(limit))):
	if limit % i == 0:
		ans = i
		limit /= i

if ans < limit:
	ans = limit

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

from lib import *

clear()

hide_cursor()

print('Challenge #5: Smallest Multiple\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

number = 80
while True:
	if(is_smallest_multiple(number)):
		ans = number
		break
	number += 80

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

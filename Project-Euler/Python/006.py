from lib import *

clear()

hide_cursor()

print('Challenge #6: Sum Square Difference\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

square_sum = sum_square = 0

for i in range(101): 
	sum_square += ( i * i )

for i in range(101):
	square_sum += i
square_sum *= square_sum

ans = square_sum - sum_square

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

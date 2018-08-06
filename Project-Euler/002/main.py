from lib import *

clear()

hide_cursor()

print('Challenge #2: Even Fibonacci Numbers\n')
input('Press ENTER to run challenge')

print('\nRunning challenge...')

timeElapsed = time.time()

ans = 0

# Place challenge code here.
# All methods must be defined above its first call, or in a separate file

fib = a = 0
b = 1

while fib < 4e6:
	fib = a + b
	a = b
	b = fib
	ans += fib if fib % 2 == 0 else 0

timeElapsed = time.time() - timeElapsed

print('Answer: {0:,}'.format(ans))
input('Completed in {0}'.format(formatTime(timeElapsed)))

show_cursor()

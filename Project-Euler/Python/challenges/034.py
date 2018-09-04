from lib import *
import time

def is_digit_fact(n):
	return n == sum(factorial(i) for i in list(map(int, str(n))))

def run():
	ans = sum(i for i in range(3, 50000) if is_digit_fact(i))
	return ans

clear()

print('Challenge #34: Digit Factorials')
print('===============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

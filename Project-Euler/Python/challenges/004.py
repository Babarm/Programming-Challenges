from lib import *
import time

def run():
	ans = 0
	for a in range(100, 1000):
		for b in range(100, 1000):
			c = a * b
			if is_palindrome(c) and ans < c:
				ans = c
	return ans

clear()

print('Challenge #4: Largest Palindrome Product')
print('========================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

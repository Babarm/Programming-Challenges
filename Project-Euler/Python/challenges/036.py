from lib import *
import time

def run():
	ans = sum(i for i in range(1000000) if is_palindrome(i) and is_palindrome(bin(i)[2:]))
	return ans

clear()

print('Challenge #36: Double-Base Palindromes')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

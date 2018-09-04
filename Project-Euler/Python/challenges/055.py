from lib import *
import time

def add_reverse(n):
	return n + int(str(n)[::-1])

def run():
	ans = 0
	for i in range(1, 10000):
		num = i
		is_lychrel = True
		for j in range(50):
			num = add_reverse(num)
			if is_palindrome(num):
				is_lychrel = False
				break
		if is_lychrel:
			ans += 1
	return ans

clear()

print('Challenge #55: Lychrel Numbers')
print('==============================\n')


input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

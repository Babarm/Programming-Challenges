from lib import *
import time

def is_divisible(num):
	return all((num[i + 1] * 100 + num[i + 2] * 10 + num[i + 3]) % p == 0 for (i, p) in enumerate([2, 3, 5, 7, 11, 13, 17]))

def run():
	return sum(int(''.join(map(str, num))) for num in permutations(list(range(10))) if is_divisible(num))

clear()

print('Challenge #43: Sub-String Divisibility')
print('======================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	return sum(map(int, str(factorial(100))))

clear()

print('Challenge #20: Factorial Digit Sum')
print('==================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

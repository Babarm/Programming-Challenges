from lib import *
import time

def run():
	old = new = 0
	with open('data/089.txt', 'r') as f:
		for line in f:
			old += len(line.strip())
			new += len(to_roman(to_arabic(line.strip())))
	return abs(old - new)

clear()

print('Challenge #89: Roman Numerals')
print('=============================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

from lib import *
import time

def run():
	ans = 0
	for a in range(200, -1, -200):
		for b in range(a, -1, -100):
			for c in range(b, -1, -50):
				for d in range(c, -1, -20):
					for e in range(d, -1, -10):
						for f in range(e, -1, -5):
							for g in range(f, -1, -2):
								ans += 1
	return ans

clear()

print('Challenge #31: Coin Sums')
print('========================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

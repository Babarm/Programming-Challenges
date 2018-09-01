from lib import *
import time

def run():
	return ''.join(str(x) for x in next(islice(sorted(list(permutations('0123456789'))), 999999, None)))

clear()

print('Challenge #24: Lexicographic Permutations')
print('=========================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

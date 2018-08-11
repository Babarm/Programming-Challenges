import challenges
from data import challengeNames
from elib import *

def run(index):

	hide_cursor()
	clear()

	challengeid = '_'
	if index < 10:
		challengeid += '00'
	elif index < 100:
		challengeid += '0'
	challengeid += str(index)

	print(challengeNames[index])
	for i in range(len(challengeNames[index])):
		print('=', end='')
	
	print('\n\nRunning...\n\n')

	timeElapsed = time.time()
	ans = getattr(challenges, challengeid)()
	timeElapsed = time.time() - timeElapsed

	print('Answer:', end=' ')
	if isinstance(ans, int):
		print('{0:,d}'.format(ans))
	elif isinstance(ans, float):
		print('{0:,.10f}'.format(ans))
	else:
		print(ans)

	print('Completed in {0}'.format(formatTime(timeElapsed)))

	input('\n\nPress ENTER to continue . . . ')

	show_cursor()
	
	return None

def run_range(start, end):
	return None

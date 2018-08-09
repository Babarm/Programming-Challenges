from engine import *

while True:
	clear()
	print('[1] Run Single Challenge')
	print('[2] Run Range of Challenges')
	print('[3] Quit')

	choice = input('Please make a selection: ')

	if choice == '1':
		clear()
		choice = input('Challenge ID to run (enter ESC to quit): ')
		if choice.upper() == 'ESC':
			continue
		else:
			run(int(choice))
	elif choice == '3':
		break

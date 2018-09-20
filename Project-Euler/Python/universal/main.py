from engine import *

names = ['# 0: Testing']

if __name__ == '__main__':
	sys.setrecursionlimit(3000)

	clear()
	
	print('Loading assets . . . ')
	i = 0
	hide_cursor()
	with open('data/names.txt', 'r') as f:
		for line in f:
			i += 1
			names.append(line.strip())
	show_cursor()

	size = 0
	for i in range(1, len(names)):
		size += len(names[i])
	input('{0:,} bytes'.format(size))

	while True:
		clear()
		choice = input('Challenge ID: ')
		if not choice:
			break
		try:
			choice = int(choice)
			if choice < 0:
				raise Exception('Negative value')

			hide_cursor()

			ans, timeElapsed = run(choice, names[choice])

			print('Answer: {0}'.format(report(ans)))
			print('Time Elapsed: {0}\n'.format(format_time(timeElapsed)))

			pause()

			show_cursor()
		except Exception as e:
			print(e)
			print('Invalid Entry: {0}'.format(choice))
			pause()

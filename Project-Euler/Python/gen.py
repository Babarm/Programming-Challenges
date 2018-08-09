with open('challenges.py', 'w') as f:
	f.write('from clib import *\n')
	f.write('from data import *\n\n')
	for i in range(500):
		line = '# {0}: \ndef _'.format(i + 1)
		if i + 1 < 10:
			line += '00'
		elif i + 1 < 100:
			line += '0'
		line += '{0}():\n'.format(i + 1)
		line += '\tans = None\n'
		line += '\treturn ans\n\n'
		f.write(line)

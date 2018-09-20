import challenges
from datetime import timedelta
import platform
import os
import sys
import time

system = platform.system()

# OS Specific Setup
if system in ['Darwin', 'Linux']:
	# UNIX
	import tty
	import termios
	def getch():
		fd = sys.stdin.fileno()
		old = termios.tcgetattr(fd)
		try:
			tty.setraw(fd)
			return sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old)
		return None
elif system in ['Windows']:
	import msvcrt
	import ctypes
	class _CursorInfo(ctypes.Structure):
		_fields_ = [('size', ctypes.c_int), ('visible', ctypes.c_byte)]



# Invalid entry point
if __name__ == '__main__':
	print('Please start the program via main.py')



# Clears the console
def clear():
	if system in ['Darwin', 'Linux']:
		os.system('clear')
	elif system in ['Windows']:
		os.system('cls')
	else:
		print('An error occurred clearing the console . . . ')
	return None



# Hides the blinking cursor
def hide_cursor():
	if system in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = False
		ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
	elif system in ['Darwin', 'Linux']:
		sys.stdout.write('\033[?25l')
		sys.stdout.flush()
	else:
		print('Error occurred in hiding cursor . . . ')
	return None



# Shows the blinking cursor
def show_cursor():
	if system in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = True
		ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
	elif system in ['Darwin', 'Linux']:
		sys.stdout.write('\033[?25h')
		sys.stdout.flush()
	else:
		print('Error occurred in showing cursor . . . ')
	return None



# Pauses the system
def pause():
	if system in ['Darwin', 'Linux']:
		print('Press any key to continue . . .')
		hide_cursor()
		getch()
		show_cursor()
	elif system in ['Windows']:
		os.system('pause')
	else:
		print('Error occured pausing execution . . .')
	return None



# Formats a timestamp into a human-readable format
def format_time(timestamp):
	timestamp *= 1e9
	timestamp = int(timestamp)
	return timedelta(microseconds=round(timestamp, -3) // 1000)



# Runs a specified challenge
def run(challengeid, cname = ''):
	name = '_' + str(challengeid)
	if cname:
		print(cname)
		for char in range(len(cname)):
			print('=', end='')
		print('\n')
		pause()
	try:
		print('\nRunning challenge . . . \n')
		timeElapsed = time.time()
		ans = getattr(challenges, name)()
		timeElapsed = time.time() - timeElapsed
	except Exception as e:
		print(e)
	return ans, timeElapsed


# Formats a value into a readable format
def report(val, dec=100):
	if isinstance(val, int):
		return '{0:,}'.format(val)
	elif isinstance(val, float):
		return '{0:,}'.format(round(val, dec))
	else:
		return val

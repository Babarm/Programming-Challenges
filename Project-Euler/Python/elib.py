import os
import platform
import sys
import time

if platform.system() in ['Windows']:
	import msvcrt
	import ctypes
	class _CursorInfo(ctypes.Structure):
		_fields_ = [("size", ctypes.c_int),
					("visible", ctypes.c_byte)]

# Clears the screen
def clear():
	system = platform.system()
	if system in ['Darwin', 'Linux']:
		os.system('clear')
	elif system in ['Windows']:
		os.system('cls')
	return None

# Formats the time elapsed into a more readable format
def formatTime(timeElapsed):
	formatedTime = None
	if timeElapsed < 0.000001:
		formattedTime = '{0:.3f} ns'.format(timeElapsed * 1000000000)
	if timeElapsed < 0.001:
		formattedTime = '{0:.3f} \u03BCs'.format(timeElapsed * 1000000)
	elif timeElapsed < 1:
		formattedTime = '{0:.3f} ms'.format(timeElapsed * 1000)
	else:
		formattedTime = '{0:,.3f} sec'.format(timeElapsed)
	return formattedTime

# Hides the cursor
def hide_cursor():
	if platform.system() in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = False
		ctypes.windll.kernel32.SetConsoleCursorInfo(handle, ctypes.byref(ci))
	elif platform.system() in ['Darwin', 'Linux']:
		sys.stdout.write("\033[?25l")
		sys.stdout.flush()
	return None

# Shows the cursor
def show_cursor():
	if platform.system() in ['Windows']:
		ci = _CursorInfo()
		handle = ctypes.windll.kernel32.GetStdHandle(-11)
		ctypes.windll.kernel32.GetConsoleCursorInfo(handle, ctypes.byref(ci))
		ci.visible = True
		ctypes.windll.kernel32.SerConsoleCursorInfo(handle, ctypes.byref(ci))
	elif platform.system() in ['Darwin', 'Linux']:
		sys.stdout.write("\033[?25h")
		sys.stdout.flush()
	return None

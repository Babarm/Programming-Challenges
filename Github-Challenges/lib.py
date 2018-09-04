import platform
import os

system = platform.system()

def clear():
	if system in ['Darwin', 'Linux']:
		os.system('clear')
	elif system in['Windows']:
		os.system('cls')
	else:
		print('Unable to clear screen')
	return None

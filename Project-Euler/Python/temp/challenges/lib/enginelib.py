import os
import platform
import sys
import time

def clear():
	system = platform.system()
	if system in ['Darwin', 'Linux']:
		os.system('clear')
	elif system in ['Windows']:
		os.system('cls')

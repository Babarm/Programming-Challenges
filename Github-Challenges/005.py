from lib import *

clear()
print('Question 5')
print('Level 1\n')
print('Define a class which has at least two methods:')
print('getString: to get a string from console input')
print('printString: to print the string in upper case')
print('Also please include a simple test function to test the class methods.\n\n')

class String:
	def __init__(self):
		self.string = ''
		return None

	def getString(self):
		self.string = input('Enter a string: ')
		return None

	def printString(self):
		print(self.string.upper())
		return None

	def test(self):
		self.getString()
		self.printString()
		return None


strObj = String()

strObj.test()

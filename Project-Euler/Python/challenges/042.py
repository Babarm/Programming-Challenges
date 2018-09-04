from lib import *
import time

def run():
	ans = 0
	
	letters = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

	triangulars = [1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66 ,78, 91, 105, 120, 136, 153, 171, 190, 210]

	with open('data/042.txt', 'r') as f:
		for line in f:
			words = line.replace('"', '').strip().split(',')
			for word in words:
				ans += 1 if sum(letters[char] for char in word) in triangulars else 0
	return ans

clear()

print('Challenge #42: Coded Triangle Numbers')
print('=====================================\n')

input('Press ENTER to run challenge . . . ')
print('')

timeElapsed = time.time()

ans = run()

report(ans)

timeElapsed = time.time() - timeElapsed

print(format_time(timeElapsed))

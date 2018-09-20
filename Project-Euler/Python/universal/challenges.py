from library import *

if __name__ == '__main__':
	print('Please start program via main.py')

def _0():
	return None

def _1():
	return sum(i for i in range(1000) if i % 3 == 0 or i % 5 == 0)
 
def _2():
	ans = a = 0
	b = fib = 1
	while fib < 4000000:
		fib = a + b
		a = b
		b = fib
		ans += fib if fib % 2 == 0 else 0
	return ans

def _3():
	ans = 0
	limit = 600851475143
	i = 2
	while i * i < limit:
		if limit % i == 0:
			limit //= i
			ans = i
		else:
			i += 1
	if limit > ans:
		ans = limit
	return ans

def _4():
	ans = 0
	for a in range(100, 1000):
		for b in range(100, 1000):
			c = a * b
			if is_palindrome(c) and ans < c:
				ans = c
	return ans
 
def _5():
	ans = 80
	while True:
		if is_smallest_multiple(ans, 20):
			break
		ans += 80
	return ans

def _6():
	return sum(i for i in range(101)) * sum(i for i in range(101)) - sum(i * i for i in range(101))

def _7():
	return nth_prime(10001)

def _8():
	data = ''
	with open('data/008.txt', 'r') as f:
		for line in f:
			data += line.strip()
	ans = 0
	for i in range(len(data) - 12):
		section = data[i:i + 13]
		ans = max(mult(map(int, section)), ans)
	return ans

def _9():
	ans = 0
	for a in range(500):
		for b in range(333):
			c = 1000 - a - b
			if a * a + b * b == c * c:
				ans = a * b * c
	return ans

def _10():
	return sum(primes(2000000))
 
def _11():
	ans = 0

	grid = []
	with open('data/011.txt', 'r') as f:
		for line in f:
			grid.append(list(map(int, line.strip().split(' '))))

	for y in range(len(grid)):
		for x in range(len(grid)):
			if x + 4 <= len(grid):
				ans = max(mult([grid[x][y], grid[x + 1][y], grid[x + 2][y], grid[x + 3][y]]), ans)
			if y + 4 <= len(grid):
				ans = max(mult([grid[x][y], grid[x][y + 1], grid[x][y + 2], grid[x][y + 3]]), ans)
			if x + 4 <= len(grid) and y + 4 <= len(grid):
				ans = max(mult([grid[x][y], grid[x + 1][y + 1], grid[x + 2][y + 2], grid[x + 3][y + 3]]), ans)
			if x - 4 >= -1 and y + 4 <= len(grid):
				ans = max(mult([grid[x][y], grid[x - 1][y + 1], grid[x - 2][y + 2], grid[x - 3][y + 3]]), ans)

	return ans

def _12():
	ans = count = 0
	i = 1
	while count < 500:
		ans += i
		count = num_divisors(ans)
		i += 1
	return ans

def _13():
	return str(sum(int(line) for line in open('data/013.txt', 'r')))[:10]

def _14():
	return max(range(1, 1000000), key=collatz)

def _15():
	return factorial(40) // (factorial(20) * factorial(20))

def _16():
	return sum(map(int, str(2**1000)))

def _17():
	return sum(len(num_to_word(i).replace(' ', '')) for i in range(1, 1001))

def _18():
	triangle = []
	with open('data/018.txt', 'r') as f:
		for line in f:
			triangle.append(list(map(int, line.strip().split(' '))))

	for i in range(len(triangle) - 2, -1, -1):
		for j in range(len(triangle[i])):
			triangle[i][j] += max(triangle[i + 1][j], triangle[i + 1][j + 1])

	return triangle[0][0]

def _19():
	return sum(1 for i in range(1901, 2001) for j in range(1, 13) if datetime.date(i, j, 1).weekday() == 6)

def _20():
	return sum(map(int, str(factorial(100))))

def _21():
	ans = 0
	for a in range(10000):
		b = sum(proper_divisors(a))
		if a == sum(proper_divisors(b)) and a != b:
			ans += a
	return ans

def _22():
	names = []
	ans = 0
	with open('data/022.txt', 'r') as f:
		for line in f:
			names = line.strip().replace('"', '').split(',')
	names = sorted(names)
	for i, name in enumerate(names):
		ans += sum(ord(i) - 64 for i in name) * (i + 1)
	return ans

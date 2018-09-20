
print('STARTING')

with open('descriptions.txt', 'w+') as desc:
	for i in range(1, 637):
		filename = 'projecteuler.net/problem=' + str(i) + '.html'
		with open(filename, 'r') as temp:
			for line in temp:
				desc.write(line)

print('DONE')

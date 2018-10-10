
with open('src/challenges.h', 'a+') as f:
	for i in range(2, 200):
		f.write('int64_t challenge-');
		if i >= 100:
			f.write(str(i))
		elif i >= 10:
			f.write('0{0}'.format(i));
		else:
			f.write('00{0}'.format(i));
		f.write('();\n')

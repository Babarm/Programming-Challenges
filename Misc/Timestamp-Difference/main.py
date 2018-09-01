

timeOne, timeTwo = map(int, input('Please enter the timestamps: ').split())

timeDiff = abs(timeOne - timeTwo)

stamp = ''

if timeDiff // 86400 > 0:
	day = timeDiff // 86400
	stamp += str(day) + ' day' + ('s ' if day > 1 else ' ')
	timeDiff %= 86400
if timeDiff // 3600 > 0:
	hr = timeDiff // 3600
	stamp += str(hr) + ' hour' + ('s ' if hr > 1 else ' ')
	timeDiff %= 3600
if timeDiff // 60 > 0:
	min = timeDiff // 60
	stamp += str(min) + ' minute' + ('s ' if min > 1 else ' ')
	timeDiff %= 60
if timeDiff > 0:
	stamp += str(timeDiff) + ' second' + ('s ' if timeDiff > 1 else '')

print(stamp)

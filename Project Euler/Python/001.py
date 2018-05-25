import time

def run():
	ans = 0
	for i in range(1000):
		if(i % 3 == 0 or i % 5 == 0):
			ans += i
	return ans


challengeID = 1
challengeName = "Multiples of 3 and 5"

print("#" + str(challengeID) + ": " + challengeName)
input("Press ENTER to run challenge . . . ")
print("")

start = time.time()

ans = run()

end = time.time()

print("Answer: {0:,d}".format(ans))

print("Completed in: {0:.3f}".format(end - start) + " sec")

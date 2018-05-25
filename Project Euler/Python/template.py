# Problem #:

import time

def run():
	ans = 0
	return ans


challengeID = 0
challengeName = ""

print("#" + str(challengeID) + ": " + challengeName)
input("Press ENTER to run challenge . . . ")
print("")

start = time.time()

ans = run()

end = time.time()

print("Answer: {0:,d}".format(ans))

print("Completed in: {0:.3f}".format(end - start) + " sec")

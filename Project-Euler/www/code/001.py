ans = 0

p = int(999 / 3)
ans += int(3 * (p * (p + 1)) / 2)

p = int(999 / 5)
ans += int(5 * (p * (p + 1)) / 2)

p = int(999 / 15)
ans -= int(15 * (p * (p + 1)) / 2)

print("{0:,}".format(ans))

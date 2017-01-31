squaretri = []

for x in range(1, 100000000):
	y = x ** 2
	if (((8 * y + 1) ** (0.5) - 1) * 0.5) % 1 == 0:
		squaretri.append(y)

print squaretri
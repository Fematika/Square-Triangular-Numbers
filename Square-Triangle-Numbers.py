x = 1
square = []
squaretri = []

def search(array, target):
	lower = 0
	upper = len(array)
	
	while lower < upper:
		x = lower + (upper - lower) / 2
		val = array[x]
		
		if target == val:
			return x
			
		elif target > val:
			if lower == x:
				return False
				break
			lower = x
			
		elif target < val:
			upper = x

for x in range(1, 100000000):
	square.append(x ** 2)
	
for n in range(1, 100000000):
	val = 0.5 * n * (n + 1)
	r = search(square, val)
	if r != False:
		squaretri.append(val)

print squaretri
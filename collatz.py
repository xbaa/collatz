"""Plain collatz formula which stops after reaching a number lower than its initial input.  Outputs the frequency of repetition and the number of separate times divided by a power of two."""
def collatz(n):
	x = n
	permut = []
	poweroftwo = 1
	while x >= n:
		if x % 2 == 0:
			x = x/2
			if x % 2 != 0 or x < n:
				permut.append(poweroftwo)
				poweroftwo = 1
			else:
				poweroftwo += 1
		else:
			x = (x * 3) + 1
	return sum(permut), len(permut)

def primes():
	list=[]
	print 2 # workaround -_-
	for n in range(2, 20):
		for divisor in range(2, 9):
			if n % divisor == 1 and divisor != n:
				list.append(n)
	print list

if __name__ == "__main__":
	primes()
	
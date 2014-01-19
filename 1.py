
def multiples():
	multiples=[]
	for n in range(0, 1000):
		if n % 3 == 0 or n % 5 == 0:
			multiples.append(n)

	print sum(multiples)
	
if __name__ == "__main__":
	multiples()
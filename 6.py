
# square all the numbers up to 100 and sum them
def squareNsum():
	nums=[]
	for n in range (0, 100+1):
		num = pow(n, 2)
		nums.append(num)
	sumofsquares = sum(nums)
	
	sumNsquare(sumofsquares)
	

# sum all the numbers up to 100 and square the result
def sumNsquare(sumofsquares):
	nums=[]
	for n in range (0, 100+1):
		nums.append(n)
	sumofnums = sum(nums)
	squareofsum = pow(sumofnums, 2)

	# get the difference
	result = squareofsum - sumofsquares
	print result
	


if __name__ == "__main__":
	squareNsum()
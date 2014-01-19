def multiples():

	result = []
	
	# we know that the smallest number that's divisible by 1-10 is 2520, so our number will be bigger than that
	# since the number we're looking for has to be a multiple of 20, we can take a step size of 20
	for n in xrange (2520, 999999999 + 1, 20):
		
		for divisor in range (20, 0, -1):
		
			if n % divisor == 0:
				if divisor == 1:
					result.append(n)
					break;
				else:
					pass;
				
			else:
				break; # that number's no good, jump back to the outer loop and start trying the next number
		
		if result:	
			print result
			break;
			
	
if __name__ == "__main__":
	multiples()
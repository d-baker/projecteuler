def multiples():

	result = []
	
	# we know that the smallest number that's divisible by 1-10 is 2520, so our number will be bigger than that
	# since the number we're looking for has to be a multiple of 20, we can take a step size of 20
	for n in xrange (2520, 999999999 + 1, 20):
		
		for divisor in range (20, 0, -1):
		
			if n % divisor == 0: # if we pass this test then the number is divible by 20
				if divisor == 1: # if we reach 1 and it's still divisible by 20, save the number
					result.append(n)
					break;
				
			else:
				break; # that number's no good, jump back to the outer loop and start trying the next number
		
		# if we got a result, print it and end the loop
		if result:	
			print result
			break;
			
	
if __name__ == "__main__":
	multiples()
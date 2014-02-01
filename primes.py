def primes(num_nums):
	primes=[2]
	
	for potential_prime in range(3, num_nums, 2): # step by 2 to avoid even numbers
		
		for divisor in range(2, potential_prime+1): # check each number against every divisor up to the number itself
			
			if potential_prime % divisor != 0:
				if divisor==potential_prime -1 : # if we reach this, the number isn't divisible by any of the divisors we've tried - so save it!
					primes.append(potential_prime)
			else:
				break

	print primes

if __name__ == "__main__":
	primes(100)

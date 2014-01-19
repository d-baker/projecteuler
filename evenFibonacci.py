
def fibonacci():
	#starting with 1 and 2
	fibSequence = [1, 2]
	
	for n in range (0, 100):
		#first iteration we just add the 2 existing terms in the list
		if n == 0:
			currentFib = fibSequence[1] + fibSequence[0]
		
		#all subsequent iterations dealt with here
		else:
			prevFib = fibSequence[n]
			currentFib = currentFib + prevFib
			
		#stop it after 4000000
		if currentFib > 4000000:
			break;
		
		#all our terms get added to a list
		fibSequence.append(currentFib)
		
	print "fibonacci sequence: ", fibSequence
	
	#call the function that finds the even ones
	evenNums = getEven(fibSequence)
	
	#sum 'em!
	print "RESULT! ", sum(evenNums)
	

def getEven(fibSequence):
	evenNums=[]
	for i in fibSequence:
		if i % 2 == 0:
			evenNums.append(i)
	print "even fibonaccis: ", evenNums
	return evenNums
	
	
if __name__ == "__main__":
	fibonacci()

	
#################################################
# erroneous pancake code discovered while failing
# http://oeis.org/A000124

for n in range (1, 100):
		if n < 2:
			currentFib = n + n
		else:
			prevFib = currentFib
			currentFib = prevFib + n
		fibSequence.append(currentFib)
	print fibSequence

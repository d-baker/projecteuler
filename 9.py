
def special_py_trip():	
	import math
	# make pairs from every combination between 1-1000 where the LH term of the pair is smaller than the RH term
	# actually this is probably unnecessary but I haven't figured out what can be eliminated yet
	pairs = []
	for a in xrange(1, 1001):
		for b in xrange(1, 1001):
			if a < b:
				pair = [a, b]
				pairs.append(pair)


	for pair in pairs:
		for n in range (0, 2): # iterate over nested lists (pairs)
			(a, b) = pair
			
		#print a, b
		c = math.log(a**2)+(b**2)
		if a+b+c == 1000 : # moment of truth
			print a*b*c
		#else:
			#print "no luck"

			
if __name__ == "__main__":
	special_py_trip()

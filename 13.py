# give it a text file with the numbers as input
# split up into a list where each newline is an item
# sum the list with a parameter for number of digits to calculate to (10)

# http://stackoverflow.com/questions/3142054/python-add-items-from-txt-file-into-a-list

def largesum():
	nums=[]
	
	file = open("bignumbers.txt", "r")
	for line in file:
		nums.append(int(line))
		
	summ = sum(nums)
	result = str(summ) # need to get the first 10 chars of this 
	print result[0:10]
	
if __name__ == "__main__":
	largesum()

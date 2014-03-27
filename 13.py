

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

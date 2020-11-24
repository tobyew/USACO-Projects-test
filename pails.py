#http://www.usaco.org/index.php?page=viewproblem2&cpid=615
#brute force
def readInput():
	with open("pails.in", "r") as f:
		inp = f.readlines()
	small = int(inp[0].split()[0].strip())
	big = int(inp[0].split()[1].strip())
	max = int(inp[0].split()[2].strip())
	return small, big, max

def bruteforce(small, big, max):
	highest = 0
	numsmall = 0
	while numsmall*small + small <= max:
		numsmall += 1
		
	numbig = 0
	while numbig*big + big <= max:
		numbig += 1
	for i in range(numsmall, -1, -1):
		total = 0
		total += small*i
		while total + big <= max:
			total += big
		if total > highest:
			highest = total
	return highest

def output(highest):
	with open("pails.out", "w+") as f:
		f.write(str(highest) + "\n")


small, big, max = readInput()
highest = bruteforce(small, big, max)
output(highest)
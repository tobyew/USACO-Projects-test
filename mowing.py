#https://docs.google.com/spreadsheets/d/1aLtI-R03TiVfZ0oO020ecraJErVdmM7a1iWiyRBROzc/edit#gid=0
def readInput():
	with open("mowing.in", "r") as f:
		inp = f.readlines()
	inp.pop(0)
	intructions = []
	for elem in inp:
		intructions.append(elem.strip())
	return intructions

def simulateMowing(intructions):
	t = 0
	fjloc = (0, 0)
	mowed = {(0, 0): 1}
	possibleTimes = []
	for elem in intructions:
		direction = elem.split()[0]
		for i in range(1, int(elem.split()[1])+1):
			if direction == 'N':
				fjloc = (fjloc[0], fjloc[1]+1)
			elif direction == 'E':
				fjloc = (fjloc[0]+1, fjloc[1])
			elif direction == 'S':
				fjloc = (fjloc[0], fjloc[1]-1)
			elif direction == 'W':
				fjloc = (fjloc[0]-1, fjloc[1])
			#if its a new place
			if fjloc not in mowed:
				mowed[fjloc] = 0
			#if its been mowed
			elif fjloc in mowed:
				possibleTimes.append(mowed[fjloc])
			t += 1

			for elem1 in mowed:
				mowed[elem1] += 1
	if len(possibleTimes) == 0:
		possibleTimes.append(-1)
	return min(possibleTimes)

def writeOutput(answer):
	with open("mowing.out", "w+") as f:
		f.write(str(answer) + '\n')
intructions = readInput()
answer = simulateMowing(intructions)
writeOutput(answer)

#debug
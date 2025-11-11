
def findBiggest(intlist):
	big = 0
	c = 0
	for j in range(len(intlist)):
		if (intlist[j] > big):
			big = intlist[j]
	return big

def biggestCount(intlist, mrbig):
	c = 0
	for j in range(len(intlist)):
		if (intlist[j] == mrbig):
			c += 1
	for i in range(c):
		intlist.remove(mrbig)
	return (intlist)

g_size = 0
intlist = [1,11,37,53,22,46,1,63,83,72,75,17,15,31,87,70,66,30,81,56,16,52,12,41,86,75,69,39,54,81,19,47,34,37,39,43,54,58,70,7,24,55,67,49,13,38,52,8,85,83,87,37,47,46,73,68,26,18,66,37,74,78,15,36,38,26,73,58,64,11,42,57,78,77,13,72,62,72,21,76,39,1,47,18,81,76,76,37,12,6,58,59,66,11,3,14,48,69,42,85]

while (len(intlist) > 0):
	mrbig = findBiggest(intlist)
	g_size += mrbig
	intlist = biggestCount(intlist, mrbig)

print(g_size)
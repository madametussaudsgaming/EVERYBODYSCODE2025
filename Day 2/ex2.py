import math

def add(list1, list2):
	list3 = [0, 0]
	list3[0] = list1[0] + list2[0]
	list3[1] = list1[1] + list2[1]
	return (list3)

def mult(list1, list2):
	list3 = [0, 0]
	list3[0] = ((list1[0] * list2[0]) - (list1[1] * list2[1]))
	list3[1] = ((list1[0] * list2[1]) + (list1[1] * list2[0]))
	return (list3)

def div(list1, list2):
	list3 = [0,0]
	list3[0] = int(list1[0] / list2[0])
	list3[1] = int(list1[1] / list2[1])
	return (list3)

g_engravements = 0
total = 0
listA = [-4511,67882]
for i in range(101):
	listA[0] = listA[0] + 10
	listA[1] = 67882
	for j in range(101):
		listA[1] = listA[1] + 10
		print(listA)
		engraved = True
		temp = [0, 0]
		for k in range(100):
			temp = mult(temp, temp)
			temp = div(temp, [100000,100000])
			temp = add(temp, listA)
			if (abs(temp[0]) > 1000000) or (abs(temp[1]) > 1000000):
				engraved = False
				break
		if engraved:
			g_engravements += 1
print(g_engravements)

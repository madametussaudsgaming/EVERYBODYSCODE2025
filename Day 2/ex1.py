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
	list3[0] = ((list1[0] // list2[0]))
	list3[1] = (list1[1] // list2[1])
	return (list3)

# there is a difference between floor division and int(division)
# -5355 // 100000 = -1 (rounds DOWN)
# int(-5355 / 100000) = 0 (truncates toward ZERO)

list1 = [0, 0]

for i in range(100):
	res1 = mult(list1, list1)
	res2 = div(res1, [10, 10])
	res3 = add(res2, [154,51])
	list1 = res3


print(list1)
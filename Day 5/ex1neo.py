

class fb_Segment:
	def __init__(self, val):
		self.value = val
		self.left = None
		self.right = None

def split_and_convert(str):
	no_id = str.split(":", 1) [1]
	int_str = no_id.split(",")
	int_list = list(map(int, int_str))
	return (int_list)

def amazon_assembly_center(list):
	ori = (fb_Segment(list[0]))
	fishbone = [ori]

	for i in (list[1:]):
		placed = False
		for segment in fishbone:
			if i < segment.value and segment.left is None:
				segment.left = i
				placed = True
				break
			elif i > segment.value and segment.right is None:
				segment.right = i
				placed = True
				break
		if placed == False:
			fishbone.append(fb_Segment(i))
	return (fishbone)

theBONE = amazon_assembly_center(split_and_convert("10:8,7,3,4,7,9,1,4,6,3,8,9,8,9,5,3,5,8,3,7,3,8,3,2,9,6,2,8,3,9"))
for i in theBONE:
	print(i.value, end = "")
print("\n", end = "")

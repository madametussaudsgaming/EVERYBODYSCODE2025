class Rule:
	def __init__(self, i, j):
		self.former = i
		self.latter = j

listnames = "Nylirin,Nylardith,Nylvyr,Nyirin,Aelvyr,Aelardith,Nyardith,Aelirin,Nyvyr".split(',')
og_Ruleset = """r > d,i
v > y
N > y
y > a,b,r
e > b
t > h
l > v,a,i
a > r
A > e
d > i
i > t,r,n"""

rules = og_Ruleset.split('\n')
rouxls = []
for i in range(len(rules)):
	rouxls.append(Rule(rules[i][0], rules[i][4:].split(',')))
	print(rouxls[i].former, rouxls[i].latter)

rouxls_card = []

for i in range(len(listnames)):
	print('\n')
	for j in range(len(listnames[i])):
		rouxls_card.clear()
		for k in range(len(rouxls)):
			if listnames[i][j] == rouxls[k].former and not(j + 1 >= len(listnames[i])):
				if listnames[i][j + 1] in rouxls[k].latter:
					print("valid")
					rouxls_card.append("valid")
					break
				else:
					print("invalid")
					rouxls_card.append("invalid")
					break
			else:
				continue
		for r in rouxls_card:
			if r == "invalid":
				print(f"{listnames[i]} ain't it")

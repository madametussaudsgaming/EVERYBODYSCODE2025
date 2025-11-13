class Rule:
	def __init__(self, i, j):
		self.former = i
		self.latter = j

listnames = "Vyrlzar,Shaemparth,Zynnylor,Vansyron,Xendphor,Elvarroth,Drazimar,Zynsyron,Zynphor,Xendparth,Elvarnylor,Skarkryth,Rythsyron,Vyrlimar,Skarroth,Xendkryth,Vyrlkryth,Xendimar,Drazparth,Draznylor,Xendzar,Drazkryth,Elvarimar,Vyrlsyron,Elvarzar,Rythimar,Skarnylor,Zynzar,Vyrlnylor,Shaemroth,Shaemnoris,Vannoris,Shaemimar,Zynparth,Skarsyron,Elvarkryth,Rythphor,Zynfyr,Rythparth,Urithphor,Vyrlphor,Drazfyr,Vanroth,Rythnylor,Vannylor,Rythzar,Rythkryth,Elvarfyr,Zynnoris,Vanparth,Vankryth,Zynroth,Xendfyr,Urithkryth,Vyrlnoris,Skarparth,Urithnoris,Shaemzar,Vyrlroth,Urithroth,Elvarnoris,Xendnylor,Elvarphor,Xendroth,Elvarparth,Vyrlfyr,Zynkryth,Shaemnylor,Rythfyr,Vanzar,Rythnoris,Skarfyr,Skarphor,Zynimar,Elvarsyron,Skarnoris,Vanfyr,Vanphor,Vanimar,Shaemfyr,Urithfyr,Skarimar,Vyrlparth,Skarzar,Xendnoris,Draznoris,Urithparth,Drazphor,Drazsyron,Shaemsyron,Drazroth,Urithsyron,Shaemphor,Xendsyron,Drazzar,Urithzar,Shaemkryth,Urithimar,Urithnylor,Rythroth".split(',')
og_Ruleset = """m > a,p,f,r,n,i,k,s,z
o > r,t,n
n > y,o,p,f,r,n,i,k,s,z,d
z > i,a,p,f,r,n,k,s,z
h > o,p,f,r,n,i,k,s,z,v
t > h
Z > y
l > v,o,p,f,r,n,i,k,s,z
k > r,v
a > z,r,v,e
S > k,h
i > m,s,t
d > p,f,r,n,i,k,s,z
U > r
E > l
y > r,l,t,v
r > a,p,f,r,o,t,n,i,k,y,s,z,l,v
s > y
f > y
D > r
V > y,a
e > m,v
R > y
p > h,a
X > e
v > a"""

rules = og_Ruleset.split('\n')
rouxls = []
for i in range(len(rules)):
	rouxls.append(Rule(rules[i][0], rules[i][4:].split(',')))
	print(rouxls[i].former, rouxls[i].latter)

rouxls_card = []
rouxls_cards = []

for i in range(len(listnames)):
	print('\n')
	rouxls_card = []
	for j in range(len(listnames[i])):
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
	rouxls_cards.append(rouxls_card)

sum = 0

for i,name in enumerate(listnames):
	if len(set(rouxls_cards[i])) == 1:
		sum += (i+1)
		print(f"{name} is fine")
	else:
		print(f"{name} is not fine")

print(sum)

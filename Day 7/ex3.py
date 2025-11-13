class Rule:
	def __init__(self, i, j):
		self.former = i
		self.latter = j

listnames = "Ny,Nyl,Nyth,Nyss,Nyrix,Rah,Har,Arak,Ryth,Fen,Xan,Ign,Shaem,Ky,Zor,Zyrix,Wyn,Ryss,Ilmar,Luth".split(',')
og_Ruleset = """u > t,v
o > r,t,v
a > r,v,k,e
L > u
e > t,v,m
R > a,y
F > e
s > s,j,r,f,p,g,o,c,n,k,z
m > j,r,f,p,g,o,c,n,k,z,a
l > j,r,f,p,g,o,c,n,k,z,v
t > h
Z > o,y
x > i,j,r,f,p,g,o,c,n,k,z
N > y
n > o,a,j,r,f,p,g,c,n,k,z
z > e
p > y
c > y
h > z,j,r,f,p,g,o,c,n,k,v
r > i,o,j,r,f,p,g,c,n,k,z,v
k > y,j,r,f,p,g,o,c,n,k,z
W > y
X > a
A > r
g > o,v
I > g,l
f > r
H > a
y > v,x,t,n
j > o
K > y
i > s,l,x
S > h"""

rules = og_Ruleset.split('\n')
rouxls = []
for i in range(len(rules)):
	rouxls.append(Rule(rules[i][0], rules[i][4:].split(',')))
	print(rouxls[i].former, rouxls[i].latter)

rouxls_card = []
rouxls_cards = []

for i in range(len(listnames)):
	rouxls_card = []
	for j in range(len(listnames[i])):
		for k in range(len(rouxls)):
			if listnames[i][j] == rouxls[k].former and not(j + 1 >= len(listnames[i])):
				if listnames[i][j + 1] in rouxls[k].latter:
					rouxls_card.append("valid")
					break
				else:
					rouxls_card.append("invalid")
					break
			else:
				continue
	rouxls_cards.append(rouxls_card)

needsremoving = 1
removed = 0
print('\n')

while (needsremoving == 1):
	needsremoving = 0
	for i,name in enumerate(listnames):
		if len(set(rouxls_cards[i])) == 1 and rouxls_cards[i][0] == "valid":
			print(f"{name} is fine")
		else:
			print(f"{name} will be removed")
			listnames.remove(name)
			rouxls_cards.pop(i)
			removed += 1
			needsremoving = 1
			break

# print(listnames)
# print(removed)
# prior is the 'remove incompatible prefixes'

rules_dict = {}
for rule in rouxls:
	rules_dict[rule.former] = rule.latter
print(rules_dict)

def recurse(current_name, rules_dict, min_len=7, max_len=11):
	results = []
	if len(current_name) >= min_len:
		results.append(current_name)
	if len(current_name) >= max_len:
		return (results)
	last_char = current_name[-1]
	if last_char in rules_dict:
		for next_char in rules_dict[last_char]:
			results.extend(recurse(current_name+next_char, rules_dict, min_len, max_len))
	return (results)

all_names = []
for name in listnames:
	all_names.extend(recurse(name, rules_dict))

for name in sorted(set(all_names)):
	print(name)
print(len(sorted(set(all_names))))
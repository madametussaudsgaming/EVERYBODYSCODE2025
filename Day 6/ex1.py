
string = "ABCCcaaCAAAbccbCAcbAaCBCaAaBCacAbAaccCcAcBcBBbCBcAaCacabaBbAcBbaccaBbCCAAbcAbbBcCbcCAcBBbAaABAcAabcc"
string = string.replace("B", "")
string = string.replace("b", "")
string = string.replace("C", "")
string = string.replace("c", "")
print(string)
A =0
a = 0

for i in range(len(string)):
	if string[i] == 'A':
		A += 1
	if string[i] == 'a':
		a += A

print (a)
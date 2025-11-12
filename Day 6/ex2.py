
string = "ABCaaCBCAAabbBbBAaCacaaACBCaBaACCCaBBBaBBcCbBCaaCaBCBacBacacAaBACaCbcBcCBcaBbCBCABBAbCbBAaBBBAaCAACcbBABcABbbaBbcAbBaccBbCCabAbABAaBAbbbcACcbbcaacAaAbcCbcBcBbcBaacAAbCBAcbBABAabBBAbAaaBaCbaAACBaaBAcbabCBCBcaaCCCbCbacCccAbAccbBccABCbaCAbAAbbcBcBaBAaAaCAcAAcBBAcccaBAbBBCbcBBcAAAbbaACbaBACCBABaaBcaBbBC"
print(string)
A =0
a = 0
B = 0
b = 0
C = 0
c = 0

for i in range(len(string)):
	if string[i] == 'A':
		A += 1
	if string[i] == 'B':
		B += 1
	if string[i] == 'C':
		C += 1
	if string[i] == 'a':
		a += A
	if string[i] == 'b':
		b += B
	if string[i] == 'c':
		c += C

print (a + b + c)

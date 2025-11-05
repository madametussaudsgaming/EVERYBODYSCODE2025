import math
import itertools

nameList = ['Harnnoris','Fyrrex','Ryngnar','Ignthyn','Eltvalir','Qyranar','Igngyth','Bryllon','Gavfeth','Elvarfelix','Beldren','Zorverax','Urakxel','Xendlyr','Galloris','Brylnyn','Karthxith','Quorverax','Elaridris','Arkroth']
i = 0
listLen = len(nameList)

def goUp(j):
    global i
    i = (i + j)%listLen
    return i

def goDown(k):
    global i
    i = (i - k)% listLen
    return i

instructions = "L6,R10,L6,R7,L9,R9,L7,R17,L15,R13,L5,R15,L5,R14,L5,R12,L5,R13,L5,R12,L8,R13,L6,R18,L11,R5,L11,R10,L15".split(",")

for instruction in instructions:
    direction = instruction[0]
    steps = int(instruction[1:])
    
    if direction[0] == 'R':
        goUp(steps)
    elif direction[0] == 'L':
        goDown(steps)

print(nameList[i])



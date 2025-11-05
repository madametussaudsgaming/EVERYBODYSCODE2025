import math
import itertools

nameList = ['Tyrdra','Quenaes','Morncoryx','Karthzryn','Syldrith','Belpyros','Brythfroth','Falnyn','Aelkyris','Caloris','Noraksyx','Urakcyth','Ralroth','Breloth','Selknoris','Urgryph','Zalyth','Palddravor','Glynndravor','Thymfarin','Quarnmirix','Nyrixcion','Elarsar','Voraxzyth','Torjor','Brelmyr','Dormyr','Gavagrath','Ilmarardith','Malthys']
i = 0
listLen = len(nameList)

def calcUp(j):
    l = (0 + j)%listLen
    return l

def calcDown(k):
    l = (0 - k)% listLen
    return l

instructions = "L14,R41,L41,R47,L42,R40,L32,R47,L16,R33,L30,R8,L9,R29,L31,R24,L23,R29,L43,R14,L5,R49,L5,R39,L5,R32,L5,R42,L5,R17,L5,R25,L5,R43,L5,R8,L5,R27,L5,R41,L27,R34,L35,R16,L29,R8,L12,R38,L25,R42,L24,R12,L38,R8,L11,R7,L15,R38,L49".split(",")

for instruction in instructions:
    direction = instruction[0]
    steps = int(instruction[1:])
    
    if direction[0] == 'R':
        copy = nameList[0]
        nameList[0] = nameList[calcUp(steps)]
        nameList[calcUp(steps)] = copy
    elif direction[0] == 'L':
        copy = nameList[0]
        nameList[0] = nameList[calcDown(steps)]
        nameList[calcDown(steps)] = copy

print(nameList[0])
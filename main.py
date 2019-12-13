#Advent of Coding 2015

import re


#Day 1 Function
def floorchange(directions):
    floor = 0
   
    for i in range(len(directions)):
        if floor == (-1):
            print(i)
       
        if directions[i] == '(':
            floor += 1
        else:
            floor -= 1
    return floor

#Day2 Part 2 
def ribbon(boxes):
    presents = (re.findall(r'(\d{1,2})x(\d{1,2})x(\d{1,2})\n',boxes))
    totrib = 0
        for x in presents:
        i = [int(y) for y in x]
        i.sort()
        totrib += (int(i[0]*2) + int(i[1]*2)) + (int(i[1]) * int(i[0]) *int(i[2]))
    print(totrib)

#Day 2 Part 1 
def presentwrap(boxes):
    wpp = []
    presents = re.findall(r'(\d{1,2})x(\d{1,2})x(\d{1,2})\n',boxes)
    totwrap = 0
    for i in presents:
        d = [int(i[0]), int(i[1]), int(i[2])]
        sas = [d[0]*d[1],d[2]*d[1],d[0]*d[2]]

        totwrap += min(sas) + 2*sas[0]+ 2*sas[2]+ 2*sas[1]
    print(totwrap)

#Part 4
def movehouse(location,direction):
    global sloc
    global rloc
    global santa
    move = {'^':[1,0],'v':[-1,0],'<':[0,-1],'>':[0,1]}
    newloc = [(location[0] + move[direction][0]),(location[1] + move[direction][1])]
    if santa == True:
        sloc = newloc
        santa = False
    else:
        rloc = newloc
        santa = True
    
    return newloc

##main for part 3

temp = open("\\inputs\\day3.txt")
direcs = temp.read()
sloc = [0,0]
rloc =[0,0]
santa = True
houses = [[0,0]]

for i in range(len(direcs)):
    if santa== True:
        newloc = movehouse(sloc,direcs[i])
    else:
        newloc = movehouse(rloc,direcs[i])
    if newloc not in houses:
    houses.append(newloc)
print(len(houses))

##main for part 2
#inputd = open("newfile.txt")
#boxes = inputd.read()
#ribbon(boxes)

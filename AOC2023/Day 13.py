import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"
part1 = False #True

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print("First Line: ",lines[0], "\n")

total = 0
finalString = ""
collect = []

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


def doPattern(pattern):
    # try horizontal
    firstLine = True
    allPoss = set()
    for line in pattern:
        #print(">>>",line)
        poss = set()
        i = 1

        while i < len(line):
            front = line[0:i]
            back = line[i:]

            m = min(len(front), len(back))
            #print(front, back)
            #print("> orig", front, back)
            #print("> fix", m, front[i-m:], back[:m][::-1])
            if front[i-m:i] == back[:m][::-1]:
                #print(i)
                poss.add(i)
                
            i += 1
        #print(">>",poss)
        if firstLine:
            allPoss = poss
            firstLine = False
        else:
            allPoss = allPoss.intersection(poss)
        #print(poss, allPoss)
        if len(allPoss) == 0:
            break
    #print("Finish",allPoss, len(allPoss))
    return allPoss

def patternHelper(pattern):

    newPattern = newPattern = [""] * len(pattern[0])
    for line in pattern:        
        i = 0
        while i < len(line):
            newPattern[i] += line[i]
            i += 1
    #print(newPattern)
    #print(doPattern(newPattern))
    #print(doPattern(pattern))
    patternAdd = 0
    horizontal = doPattern(pattern)
    vertical = doPattern(newPattern)
    if len(horizontal) > 0:
        patternAdd += horizontal.pop()
    if len(vertical) > 0:
        patternAdd += vertical.pop() * 100
    
    #pattern = doPattern(newPattern) | doPattern(pattern)
    #print(pattern)
    return patternAdd

def turn(pattern):
    newPattern = newPattern = [""] * len(pattern[0])
    for line in pattern:        
        i = 0
        while i < len(line):
            newPattern[i] += line[i]
            i += 1
    return newPattern

def patternHelper2(pattern):    
    i = 0
    firstH = doPattern(pattern)
    firstV = doPattern(turn(pattern))

    while i < len(pattern):
        line = pattern[i]
        j = 0
        while j < len(line):



            original = pattern[i][j]
            if original == "#":
                pattern[i][j] = "."
            else:
                pattern[i][j] = "#"

            

            horizontal = doPattern(pattern)

            if len(horizontal.difference(firstH)) > 0:
                print(horizontal)
                return horizontal.difference(firstH).pop()
            
            vertical = doPattern(turn(pattern))
            if len(vertical.difference(firstV)) > 0:
                print(vertical)
                return vertical.difference(firstV).pop() * 100
            
            pattern[i][j] = original
            print(i,j)
            j += 1
        i += 1
        


patterns = []
for line in lines:

    if line == "":
        print('start 1')
        collect.append(patternHelper2(patterns))
        patterns = []
    else:
        patterns.append([x for x in line])

collect.append(patternHelper2(patterns))

print("Part1:",sum(collect), collect)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))

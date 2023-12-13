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

def getPoss(springs, cond, condNum = 0):
    poss = 0
    if condNum > len(cond) - 1:
        if "#" not in springs:
            return 1
        else:
            return 0
    
    condition = cond[condNum]
    i = 0
    while i < len(springs):
        
        nextSprings = springs[i: i + condition]
        restOfSpring = springs[i + condition:]

        # check the upcoming string based on conditions
        if (not "." in nextSprings and len(nextSprings) == condition): 

            # check on the single string value after the upcoming string
            if restOfSpring == '' or restOfSpring[0] in "?.":
                poss += getPoss(springs[i + condition + 1:], cond, condNum + 1)

        if springs[i] == "#":
            break
        i += 1
    return poss

lineNum = 15
#for line in lines[lineNum:lineNum + 1]:
j = lineNum

for line in lines[lineNum:16]:
    springs, instrStr = line.split(" ")
    cond = [int(x) for x in instrStr.split(",")]

    springs = "?".join([springs] * 5)
    cond = cond * 5

    possNum = getPoss(springs, cond)
    collect.append(possNum)
    
    print(j, possNum, springs)
    j += 1

print("Part1:",sum(collect), collect)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))

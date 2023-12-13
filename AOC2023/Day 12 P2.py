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

def getPoss(springs, cond):

    # storing space
    # column is the condition and possibility of existence
        # every value in the column is the location (spring list) and possibility (0/1)
        # each subsequent (reverse) looks at the next column to determine possibilities (and location)

    saved = []
    for i in range(0, len(springs)):
        saved.append([0] * len(cond))

    condPlace = 0
    while condPlace < len(cond):

        # column we're iterating down
        condNum = len(cond) - 1 - condPlace

        # expected springs that are good
        currentCond = cond[condNum]

        #print('current cond num:', condNum, currentCond)

        spring_iter = 0
        while spring_iter < len(springs):

            # past the end of spring length
            if currentCond + spring_iter > len(springs):
                break
            
            success = True
            
            # iterate through condition to check, should be #/?
            for cond_iter in range(0,currentCond):
                if springs[spring_iter + cond_iter] == ".":
                    success = False
            
            if condPlace > 0 and (spring_iter + currentCond > len(springs) - 1 or springs[spring_iter + currentCond] == "#"):
                success = False

            # if there is # after the last spot, it fails
            if condPlace == 0 and "#" in springs[spring_iter + currentCond:]:
                success = False           

            if success:
                if condPlace == 0:
                    saved[spring_iter][condNum] = 1
                else:
                    subtotal = 0

                    condOverSpring = spring_iter + currentCond + 1
                    
                    while condOverSpring < len(springs):
                        # add the next line of condition column to current
                        subtotal += saved[condOverSpring][condNum + 1]
                        #if subtotal > 0:
                        #print(condNum, condOverSpring, subtotal)
                        if springs[condOverSpring] == "#":
                            break
                        condOverSpring += 1
                    saved[spring_iter][condNum] = subtotal

                    # iter = cond[j]
                    # i = spring iterate
                    # j2 is iterating iter
            
            spring_iter += 1
        condPlace += 1

    i = 0
    total = 0
    while i < len(springs):
        total += saved[i][0]

        # last possible place for starting
        if springs[i] == "#":
            break
        i += 1

    #total = sum([x[0] for x in saved])
    return total

for line in lines:
    springs, instrStr = line.split(" ")
    cond = [int(x) for x in instrStr.split(",")]

    springs = "?".join([springs] * 5)
    cond = cond * 5

    #possNum = getPoss(springs, cond)
    collect.append(getPoss(springs, cond))

print("Part 2:",sum(collect), collect)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))

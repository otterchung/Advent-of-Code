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

mat = [[]] #line length by cond length
for line in lines[:1]:
    springs, instrStr = line.split(" ")
    cond = [int(x) for x in instrStr.split(",")]

    

    springs = "?".join([springs] * 5)
    cond = cond * 5

    mat = []
    # for i in range(0, len(cond)):
    #     mat.append([0] * len(springs))
    for i in range(0, len(springs)):
        mat.append([0] * len(cond))

    # find last spot
    i = 0
    while i < len(mat):
        #print('hello', i)
        iter = cond[len(cond) - 1] #cond[-1]

        if (i + iter > len(springs)):
            #print('broke')
            break

        good = 1
        j = 0
        while j < iter:
            if (springs[i + j] == "."):
                #print('zero', i+j)
                good = 0
            j += 1
        

        # if the rest of string has #, then false
        j = i + iter
        while j < len(springs):
            if springs[j] == "#":
                #print('zero2', j)
                good = 0
            j += 1

        if good == 1:
            mat[i][len(cond) - 1] = 1
            #print(i, len(cond) - 1)

        
        i += 1 

    #calculating other spots
    j = len(cond) - 2
    while j >= 0:

        iter = cond[j]
        #print(j)
        i = 0
        while i < len(springs):
            if i + iter + 1 > len(springs):
                break
            #print("i", i)
            good = 1
            j2 = 0

            # check last, does it fit?
            while j2 < iter:
                if springs[i + j2] == ".":
                    good = 0
                    break
                j2 += 1

            # if fits, is the next element "#", fail it
            if(springs[i + iter] == "#"):
                good = 0

            if good == 0:
                i += 1
                continue

            subtotal = 0

            # still good?
            j2 = i + iter + 1
            while j2 < len(springs):
                subtotal += mat[j2][j+1]
                if springs[j2] == "#":
                    #print('j stuck')
                    break
                j2 += 1

            # i tracks springs
            # j tracks condition?
            mat[i][j] = subtotal 
              
            i += 1
        j -= 1

    total = 0
    i = 0
    while i < len(springs):
        total += mat[i][0]

        if (springs[i] == "#"):
            break
        i += 1
    
    collect.append(total)
print("Part1:",sum(collect), collect)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))

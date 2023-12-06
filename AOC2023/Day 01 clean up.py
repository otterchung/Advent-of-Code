import os

if "Files/Random Codes/AOC2023" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
#data = "actual"

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print('first line:',lines[0], "\n")

def findFirstNum(arr, isReverse):
    poss = []
    found = ""
    for a in arr:

        if a in numline:
            return a
        
        i = 0
        while i < len(poss):

            if not isReverse:
                poss[i] += a
            else:
                poss[i] = a + poss[i]

            if poss[i] in numArr:
                return str(1+numArr.index(poss[i]))
            i += 1
        poss.append(a)
    
    return found

total = 0
finalString = ""
collect = []

numline = "123456789"
newnum = "one,two,three,four,five,six,seven,eight,nine,ten"
numArr = newnum.split(",")

for line in lines:

    first = findFirstNum([x for x in line], False)
    
    rline = [x for x in line]
    rline.reverse()

    second = findFirstNum(rline, True)

    total = int(first + second)
    collect.append(total)

print(collect)
print(sum(collect))
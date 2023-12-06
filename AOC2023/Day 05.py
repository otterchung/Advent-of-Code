import os

if "Files/Random Codes/AOC2023" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
# data = "actual"

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print(lines[0], "\n")

total = 0
finalString = ""
collect = []

seeds = [int(x) for x in "79 14 55 13".split(" ")]

seed = """50 98 2
52 50 48"""

soil = """0 15 37
37 52 2
39 0 15"""

fertilizer = """49 53 8
0 11 42
42 0 7
57 7 4"""

water = """88 18 7
18 25 70"""

light = """45 77 23
81 45 19
68 64 13"""

temperature = """0 69 1
1 0 69"""

humidity = """60 56 37
56 93 4"""

# where each element is just the string (hand parsed) to variable
dictionaries = [seed, soil, fertilizer, water,light,temperature, humidity]

def reparse(dictionary):
    lines = dictionary.split("\n")
    allInOne = []
    for line in lines:
        dest, source, ran = [int(x) for x in line.split(" ")]
        
        allInOne.append([source,dest,ran])
    allInOne.sort()
    return allInOne


allThings = []
for di in dictionaries:
    allThings.append(reparse(di))

findTheseValue = []

def getNextVal(allThings, range, i):
    if i < len(allThings):
        
        allThing = allThings[i]

        low, high = range
        newRanges = []
        j = 0
        for s, d, add in allThing:
            add2 = (d-s)
            #print("~",d,s,add)
            sR = [s,s+add-1]
            #print("~",sR)
            #print("~",range)
            j += 1
            if low >= sR[0] and high <= sR[1]:
                newRanges.append([low+add2, high+add2])
            else:
                if low >= sR[0] and low <= sR[1]:
                    newRanges.append([low+add2, sR[1]+add2])
                
                if low <= sR[0] and high >=sR[1]:
                    newRanges.append([sR[0] + add2, sR[1] + add2])

                if high >= sR[0] and high <= sR[1]:
                    newRanges.append([sR[0]+add2, high+add2])               
        
        if high > allThing[-1][0] + add:
            #print('high too high')
            if low > allThing[-1][0] + add:
                newRanges.append([low, high])
            else:
                newRanges.append([allThing[-1][0] + add,high])
            
        if low < allThing[0][0]:
            #print('low too low')
            if high < allThing[0][0] + add - 1:
                newRanges.append([low, high - 1])
            else:
                newRanges.append([low, allThing[0][0] + add -1])
        
        #print(newRanges)
        for range in newRanges:
            if i == len(allThings) - 1:
                findTheseValue.append(range[0])
            else:
                getNextVal(allThings, range, i+1)

i = 0
while i < len(seeds):
    seedRange = [seeds[i], seeds[i] + seeds[i+1]-1]
    getNextVal(allThings, seedRange, 0)
    i += 2

print(">>",min(findTheseValue))
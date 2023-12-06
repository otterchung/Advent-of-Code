import os

if "Files/Random Codes/AOC2023" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "SampleInput.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "Input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print(lines[0])

total = 0
finalString = ""
collect = []


# helps to capture distinct numbers to prevent duplicate counting
class number:
    coors = []
    num = ""
    taken = False

    def __init__(self, coor, num):
        self.addOn(coor, num)
    
    def addOn(self, coor, num):
        self.coors.append(coor)
        self.num += num

numDict = dict()
symbols = []


# first parse -- determine where symbols and numbers are (by coordinates)
# each coordinate points to a number record (M:1)
nums = "1234567890"
i = 0
while i < len(lines):
    j = 0
    while j < len(lines[i]):
        if lines[i][j] in nums:
            newNum = number((i,j), lines[i][j])
            numDict[(i,j)] = newNum
            j += 1
            while j < len(lines[i]) and lines[i][j] in nums:
                newNum.addOn((i,j), lines[i][j])
                numDict[(i,j)] = newNum
                j += 1
            
        if j < len(lines[i]) and not lines[i][j] == '.':
            symbols.append((i,j))
        j += 1

    i += 1

# iterate through symbols, locating unused number records
total = 0
total_2 = 0
for symbol in symbols:
    x,y = symbol
    gears = set()
    for a in [-1,0,1]:
        for b in [-1,0,1]:
            i = x + a
            j = y + b
            if (i,j) in numDict.keys():

                # part 1
                if not numDict[(i,j)].taken:
                    total += int(numDict[(i,j)].num)
                    numDict[(i,j)].taken = True

                # part 2
                gears.add(numDict[(i,j)])

    gearVal = 1
    if len(gears) > 1:
        print(gears)
        for gear in gears:
            gearVal *= int(gear.num)
        total_2 += gearVal

print(total)
print(total_2)
import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
#data = "actual"
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

def splitByRange(line):
    splitRange = []
    i = 0
    prev_i = 0
    y = line.count("#")
    for a in range(0, y):
        # ....# ""# 
        i = line.index("#", i) + 1
        splitRange.append(line[prev_i:i])
        print(line[prev_i:i])
        prev_i = i
        
    return splitRange

def countLoad(ranges, start):
    total = 0
    for r in ranges:
        ohs = r.count("O")
        total += (start + start-ohs+1)/2 * ohs
        start -= len(r)

    print(total)
    return total


# flip it, going west now
map = []
for line in lines[0]:
    map.append([""] * len(lines))

i = 0
while i < len(lines):
    j = 0
    while j < len(lines):
        map[j][i] = lines[i][j]
        j += 1
    i += 1

for line in map:
    line = line + ["#"]
    ranges = splitByRange(line)

    start = len(line) -1

    collect.append(countLoad(ranges, start))


print("Part1:",sum(collect), collect)

# 8212 too high - answer: 7541
#print(line)
#print("\t".join([x for x in springs]))

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

# Day 4
scratch = dict()

for j in range(0,len(lines)):
    scratch[j] = 1

i = 0
for line in lines:
    card = line.split(":")
    winners, mine = card[1].split("|")

    winners = winners.strip()
    mine = mine.strip()
    winNum = [x.strip() for x in winners.split(" ")]
    mineNum = [x.strip() for x in mine.split(" ")]

    existing = scratch[i]

    matchPoints = 1
    matchNum = 0
    for m in mineNum:
        # Found out in Python, I was creating extra '' in my array on the split due to the spacing
        if m in winNum and m != '':
            matchPoints *= 2
            matchNum += 1
    
    # Part 1
    if matchPoints >= 2:
        total += int(matchPoints/2)

    # Part 2
    if matchNum >= 1:
        for x in range(1,matchNum+1):
            scratch[x+i] += 1 * existing
    i += 1

print('Total (Part 1):', total)
print('Collection (Part 2):', sum(scratch.values()))
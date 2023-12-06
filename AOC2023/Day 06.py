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

print(lines[0], "\n")

total = 0
finalString = ""
collect = []

arrays = []
for line in lines:
    lineString = line.split(":")[1].strip()
    # Part 1 (replaced "  " with " ")
    # Part 2 Parse (doesn't need while loop)
    while lineString.find(" ") != -1:
        lineString = lineString.replace(" ", "")
    arrays.append([int(x) for x in lineString.split(" ")])

times, distances = arrays
i = 0
while i < len(times):
    time = times[i]
    dist = distances[i]
    margin = 0
    hold = 0

    marginStart = None
    marginEnd = None

    while hold < time:
        possDist = hold * (time - hold)
        if possDist > dist:
            marginStart = hold
            hold = time
        hold += 1
    
    hold = time
    while hold > 0:
        possDist = hold * (time - hold)
        if possDist > dist:
            marginEnd = hold
            hold = 0
        hold -= 1

    i += 1
    collect.append(marginEnd - marginStart + 1)

aggregate = 1
for i in collect:
    aggregate *= i
print(">", aggregate)
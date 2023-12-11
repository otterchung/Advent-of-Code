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

def getNextSequence(sequence):
    newSequence = []
    i = 1
    while i < len(sequence):
        diff = sequence[i] - sequence[i - 1]
        newSequence.append(diff)
        i += 1
    print(newSequence)
    return newSequence
    

totals = []
totals2 = []
for line in lines:
    sequence = [[int(x) for x in line.split(" ")]]
    print('new', sequence)

    while set(sequence[-1]) != set([0]):
        sequence.append(getNextSequence(sequence[-1]))

    total = 0
    total2 = 0
    i = len(sequence)-1
    while i >= 0:
        total += sequence[i][-1]
        total2 = sequence[i][0] - total2
        i -= 1
    totals.append(total)
    totals2.append(total2)

print("Part1:",totals)
print(sum(totals))

print("Part2:",totals2)
print(sum(totals2))
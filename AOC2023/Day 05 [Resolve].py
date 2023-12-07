import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
data = "actual"

if "sample" == data:
    print(">>> YOU ARE USING SAMPLE DATA ")
    theFileName = "5-sample.txt"
else:
    print(">>> YOU ARE USING ACTUAL DATA ")
    theFileName = "5-input.txt"
print("...\n\n")

theInput = open(theFileName).read()
lines = theInput.split("\n")

print(lines[0], "\n")

# Parsing, deriving instructions list
seedRanges = []
steps = []
i = 0
while i < len(lines):
    line = lines[i]
    if i == 0:
        seeds = [int(x) for x in line.replace("seeds: ","").split(" ")]
        seedIter = 0
        while  seedIter < len(seeds):
            seedVal = seeds[seedIter]
            seedRange = seeds[seedIter + 1]
            seedRanges.append([seedVal, seedVal + seedRange - 1])
            seedIter += 2
        seedRanges.sort()
    elif i > 1:
        if "map" in line:
            instructionRanges = []
        elif "" == line:
            instructionRanges.sort()
            steps.append(instructionRanges)
        else:
            d, s, ran = [int(x) for x in line.split(" ")]
            instructionRanges.append([s, d, ran])
    i += 1

# missing last set of instructions:
instructionRanges.sort()
steps.append(instructionRanges)

# To make the instructions more readable
class info:

    def __init__(self, instructionRange):
        source, dest, range = instructionRange
        delta = dest - source
        self.sourceRange = [source, source + range - 1]
        self.delta = delta
        self.sourceLow = source
        self.sourceHigh = source + range -1

#Testing
#print("All Range:",seedRanges)
#seedRanges = seedRanges[1:]

# Iterate through the steps (converting the ranges from seed -> soil -> fertilizer, etc.)
# Per range, compare it to the instructions (range transformations) in each step
for step in steps:
    
    transformInstruction = []
    for instruction in step:
        transformInstruction.append(info(instruction))
    
    newRange = []

    for seedRange in seedRanges:
        #print("Start:",seedRange)
        low, high = seedRange

        # low lower than first instruction, stays source value
        if low < transformInstruction[0].sourceLow:
            if high > transformInstruction[0].sourceLow:
                newRange.append([low, transformInstruction[0].sourceLow - 1])
            else:
                newRange.append([low, high])

        # high higher than last instruction, 
        if high > transformInstruction[-1].sourceHigh:
            if low < transformInstruction[-1].sourceHigh:
                newRange.append([transformInstruction[-1].sourceHigh + 1, high])
            else:
                newRange.append([low, high])

        for step in transformInstruction:
            #print(step.sourceRange, step.delta)
            if low >= step.sourceLow and high <= step.sourceHigh:
                newRange.append([low + step.delta, high + step.delta])
            else:
                # low falls in range (but determined that high was higher)
                if low >= step.sourceLow and low <= step.sourceHigh:
                    newRange.append([low + step.delta, step.sourceHigh + step.delta])
                # high falls in range (but determined that low was lower)
                if high >= step.sourceLow and high <= step.sourceHigh:
                    newRange.append([step.sourceLow + step.delta, high + step.delta])
                
                # low and high fall outside the range, so, entire instruction is captured
                if low <= step.sourceLow and high >= step.sourceHigh:
                    newRange.append([step.sourceLow + step.delta, step.sourceHigh + step.delta])

    #print("Finish:",newRange)
    seedRanges = newRange

#print(">>",seedRanges)
print("Answer:",min([x for x,y in seedRanges]))




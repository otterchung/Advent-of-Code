import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

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

print("First Line: ",lines[0], "\n")

finalString = ""
collect = []

# -----------------------

class cards:
    def __init__(self, line):
        hand, points = [x for x in line.strip().split(" ")]
        handArr = [x for x in hand]

        valueDict = { "T":10, "J":11, "Q":12 , "K":13, "A": 14}

        if isPart2:
            valueDict["J"] = 0

        for x in "123456789":
            valueDict[x] = int(x)

        self.counts = {x:[] for x in range(1,6)}
        
        # get hand value based off of type (five of a kind)
        numJ = 0
        for card in set(handArr):
            if card == "J" and isPart2:
                numJ = handArr.count("J")
            else:
                self.counts[handArr.count(card)].append(valueDict[card])

        # get secondary hand value based off of card values
        arbValStr = ""
        for card in handArr:
            cardValue = str(valueDict[card])
            arbValStr += (2-len(cardValue)) * "0" + cardValue

        # build hand-type value
        uniques = 0
        arbCountStr = ""
        for i in reversed(range(1,6)):
            values = self.counts[i]
            if len(values) > 0:
                for value in values:
                    arbCountStr += str(i + numJ)
                    uniques += 1
                    numJ = 0

        # build and append hand values to the hand-type
        self.arbVal = int(arbCountStr + "0" * (5 - uniques) + arbValStr)

        if numJ == 5:
            #special case of JJJJJ
            self.arbVal = 500000000000000
            
        self.points = int(points)

for isPart2 in False, True:
    allHands = dict()
    arbVal = []

    for line in lines:
        hand = cards(line)
        arbVal.append(hand.arbVal)
        allHands[hand.arbVal] = [hand.points]#, line, hand.counts]
        
    arbVal.sort()
    i = 1
    total = 0
    for arr in arbVal:
        total += i * allHands[arr][0]
        i += 1

    print("Answer for isPart2", isPart2, total)

# Part 1: 250347426
# Part 2: 251224870
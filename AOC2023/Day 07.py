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

total = 0
finalString = ""
collect = []

# -----------------------

part2 = False
class cards:
    def __init__(self, line):
        hand, points = [x for x in line.strip().split(" ")]
        handArr = [x for x in hand]

        valueDict = { "T":10, "J":11, "Q":12 , "K":13, "A": 14}

        if part2:
            valueDict["J"] = 0

        for x in "123456789":
            valueDict[x] = int(x)

        self.counts = {x:[] for x in range(1,6)}
        
        # get hand value based off of type (five of a kind)
        numJ = 0
        for card in set(handArr):
            if card == "J" and part2:
                numJ = handArr.count("J")
            else:
                self.counts[handArr.count(card)].append(valueDict[card])

        # get secondary hand value based off of card values
        arbValStr = ""
        for card in handArr:
            cardValue = str(valueDict[card])
            arbValStr += (2-len(cardValue)) * "0" + cardValue

        self.points = int(points)

        arbCountStr = ""
        i = 5
        j = 5
        while i > 0:
            if len(self.counts[i]) > 0:                       
                for card in self.counts[i]:
                    j -= 1                 
                    arbCountStr += str(i + numJ)
                    numJ = 0
            i -= 1
        
        #special case of JJJJJ
        if numJ == 5:
            self.arbVal = 500000000000000
        else:
            self.arbVal = int(arbCountStr + "0" * j + arbValStr)

allHands = dict()
arbVal = []
for line in lines:
    hand = cards(line)
    arbVal.append(hand.arbVal)
    allHands[hand.arbVal] = [hand.points]#, line, hand.counts]
    
arbVal.sort()
i = 1
for arr in arbVal:
    total += i * allHands[arr][0]
    i += 1

print("Answer:", total)

# Part 1: 250347426
# Part 2: 251224870
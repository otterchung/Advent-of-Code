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

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

lengthTotals = 0
areaTotals = 0

x = 0
for line in lines:

    # part 1
    direction, mag, color = line.split(" ")
    mag = int(mag)
    
    if not part1:
        # part 2
        color = color.strip("()")
        directionDict = {0: "R", 1: "D", 2: "L", 3: "U"}
        direction = directionDict[int(color[-1])]

        mag = int(color[1:-1], 16)

    if direction == "R":       
        areaTotals += mag * x
    
    if direction == "L":     
        areaTotals -= mag * x

    if direction == "U":  
        x -= int(mag)    

    if direction == "D":  
        x += int(mag)  
    
    lengthTotals += mag
    
#------

print(abs(areaTotals) + lengthTotals/2 + 1)
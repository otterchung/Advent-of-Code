import os

if "Files/Random Codes/AOC2022" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2022")

print(os.getcwd())

def sumStr(arr):
    total = 0
    for a in arr:
        total += int(a)
    return total

theInput = open("Input").read()

lines = theInput.split("\n")

sumArr = [sum([int(a) for a in arr.split("\n")]) for arr in [arrs for arrs in theInput.split("\n\n")]]
print(sumArr)
print('Ans1:', max(sumArr))

sumArr.sort()
print('Ans2:', sum(sumArr[-3:]))
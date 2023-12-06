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

# setup = {
#     "red":12,
#     "green":13,
#     "blue":14
# }
for line in lines:
    id, game = line.split(":")

    idNum = int(id.split(" ")[1])
    sets = game.split(";")

    notPossible = 0

    setup = {
        "red":0,
        "green":0,
        "blue":0
    }   
    for set in sets:
        balls = set.split(",")

        for ball in balls:
            ball = ball.strip()

            num, color = ball.split(" ")
            
            if int(num) > setup[color]:
                setup[color] = int(num)
    # if notPossible == 0:
    #     collect.append(idNum)
    i = 1
    for val in setup.values():
        i *= val
    collect.append(i)

print(collect)
print(sum(collect))
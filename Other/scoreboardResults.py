import os

if "Files/Random Codes/AOC2023" not in os.getcwd():
    os.chdir("Files/Random Codes/AOC2023")

print(os.getcwd(), "\n\n...")

theFileName = "scoreboard.json"

theInput = open(theFileName).read()
#lines = theInput.split("\n")



import os

if "AOC2023" not in os.getcwd():
    os.chdir("AOC2023")

print(os.getcwd(), "\n\n...")

data = "sample"
#data = "actual"
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

next = False
workflowDict = dict()
ratings = []


class device:

    def __init__(self, nodeType):
        self.type = nodeType
        
        if self.type == "%":
            self.power = 0 # 0 is off

        if self.type == "%":
            self.remember = "low"
    
    def pulse(self, freq):
        if freq == "low" and self.type == "%":
            self.power = (self.power + 1) % 2

            if self.power == 1:
                return "high"
            
            if self.power == 0:
                return "low"


devices = dict() # nodeName -> node
paths = dict() # nodeName -> [nodeNames]
for line in lines:
    node1, nodes2 = line.split(" -> ")

    nextNodes = nodes2.split(", ")
    if node1[0] == "%":
        devices[node1[1:]] = device("%", nextNodes)
        paths[node1[1:]] = nextNodes
    elif node1[0] == "&":
        devices[node1[1:]] = device("&", nextNodes)
        paths[node1[1:]] = nextNodes
    else:
        devices[node1] = device(None, nextNodes)
        paths[node1] = nextNodes


    



print("Collections:", sum(collect), collect)
print("Intersections", sum(intersections)/2, intersections)
print("Total:", sum(collect) - sum(intersections)/2)
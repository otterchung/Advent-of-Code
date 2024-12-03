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
for line in lines:
    if line == "":
        next = True
    elif next:
        ratings1 = line.strip("{}").split(",")
        ratings.append({x.split("=")[0]: int(x.split("=")[1]) for x in ratings1})
    else:
        wName, workflow1 = line.strip("}").split("{")
        
        rules = workflow1.split(",")

        ruleArr = []
        for r in rules:
            rule = None
            if ">" in r or "<" in r:
                _if, _else = r.split(":")
                rule = _if[0], _if[1], int(_if[2:]), _else
            else:
                rule = r
            ruleArr.append(rule)



        workflowDict[wName] = ruleArr
#------

def getNext(rating, workflowName):
    workflow = workflowDict[workflowName]
    #print(workflowName, workflow)
    for flow in workflow:
        if 'tuple' in str(type(flow)):            
            var, check, val, result = flow
            if check == "<" and rating[var] < val:
                return result
            elif check == ">" and rating[var] > val:
                return result
        elif 'str' in str(type(flow)):
            return flow
        else:
            print("Bad:", flow)
        
collect = []
for rating in ratings:
    #print(rating)
    result = "in"
    while result not in ("A", "R"):
        result = getNext(rating, result)
        #print(">", result)
    if result == "A":
        collect.append(sum(rating.values()))
    #print(result)

print("P1:",sum(collect))

#------ P2 ------

# x, m, a, s... 1:4000
# distinct combinations result in A...



# start looking at A, lead up to it has to be all falses
    # ex:   px
            # m > 2090: A   means: m > 2090
            # a < 2006      means: a >= 2006         
# find what the entry is from there
    # ex:   to get to px (parse through all 4th elements of tuples)
            # in 
            # s<1351        means: s<1351

wf2 = dict() # to get to NAME, the following has to be true

# forward (actually backwards) "A" ---> crn ---> qkq ---> px ---> in

forwardDict = dict() # A --> B ---> x
trueValues = dict() # (A,crn) -> ranges
for name, workflow in workflowDict.items():
    negatives = dict()
    for flow in workflow:
        result = None
        negMin, negMax = None, None
        if 'tuple' in str(type(flow)):
            var, check, val, result = flow

            if (result, name) not in trueValues.keys():
                trueValues[(result, name)] = dict()

            if check == "<":
                vmin = 0 # 0 -> val - 1
                vmax = val - 1
                negMin = val # val -> 4000
                negMax = 4000
            elif check == ">":
                vmax = 4000 # val + 1 -> 4000
                vmin = val + 1
                negMin = 0 # 0 -> val
                negMax = val



        if 'str' in str(type(flow)):
            result = flow
            vmin, vmax = None, None
            negMin, negMax = None, None

        # handle trueValues
        if (result, name) not in trueValues.keys():
            trueValues[(result, name)] = dict()

        for key,value in negatives.items():

            if key not in trueValues[(result, name)].keys(): #!
                trueValues[(result, name)][key] = [] #!
            #trueValues[(result, name)][key] = value
            trueValues[(result, name)][key].append(value)

        if var not in trueValues[(result, name)].keys(): #!
            trueValues[(result, name)][var] = [] #!
        #trueValues[(result, name)][var] = vmin, vmax
        trueValues[(result, name)][var].append((vmin, vmax))

        negatives[var] =  negMin, negMax
        
        if result not in forwardDict.keys():
            forwardDict[result] = set()
        forwardDict[result].add(name)



# find A -> in
allPaths = []
def getPath(node, pathing = []):
    for val in forwardDict[node]:
        newPath = pathing + [val]
        if val in pathing:
            continue
        if val == "in":
            allPaths.append(newPath)
            #return newPath
        else:
            getPath(val, newPath)

getPath("A", ["A"])

# newTrueValue = dict()
# for key, values in trueValues.item():
#     for letter in "xmas":

        
allPoss = []
for path in allPaths:

    posses = [{x:(0,4000) for x in "xmas"}]

    #print(path)
    i = 1
    while i < len(path):
        #print(path[i-1], path[i])

        if (path[i-1],path[i]) in trueValues.keys():
            #print(trueValues[(path[i-1],path[i])])
            for var, rs in trueValues[(path[i-1],path[i])].items():
                    
                for r in rs:
                #!  #create new path
                    for poss in posses:
                        possMin, possMax = poss[var]

                        if r[0] != None and possMin < r[0]:
                            possMin = r[0]
                        if r[1] != None and possMax > r[1]:
                            possMax = r[1]

                        #print(">", poss[var], var, r)
                        poss[var] = (possMin, possMax)
                        #print(poss[var])
                
        else:
            print('dead end')
            break
        i += 1

    allPoss.append(poss)
    #print(poss)

# build paths....

# def buildPath(path, instructions):
#     i = 1
#     while i < len(path):
#         if (path[i-1],path[i]) in trueValues.keys():
#             for var, rs in trueValues[(path[i-1],path[i])].items():
#                 for r in rs:
#                     buildPath(instructions.append(r))
#         else:
#             print('dead end')
#             break
#         i += 1



# optionPaths = []
# for path in allPaths:
#     optionPaths.append( buildPath(path) , [{x:(0,4000) for x in "xmas"}])


collect = []    
for p in allPoss:
    mult = 1
    for vmin,vmax in p.values():
        mult *= (vmax-vmin)
    collect.append(mult)
print(sum(collect))

finalPoss = {x:[] for x in "xmas"}


# collections = set()
# for p in allPoss:
#     possSet = set()
#     for i in range(p["x"][0], p["x"][1] + 1):
#         for j in range(p["m"][0], p["m"][1] + 1):
#             for k in range(p["a"][0], p["a"][1] + 1):
#                 for l in range(p["s"][0], p["s"][1] + 1):
#                     collections.add( (i,j,k,l) )
#     print("next P")
# print(len(collections))

# maxVal = 4000
# minVal = 0
# for name, workflow in workflowDict.items():



#     for flow in workflow:
#         # px:
#         #     - qkq, a:[0,2006]
#         #     - A, m:[2091,4000], a:[2007:4000] 
#         #     - rfg, m:[0,2090], a:[0:2006]
#         if 'tuple' in str(type(flow)):            
#             var, check, val, result = flow
#             if check == "<":
#                 positive = {result: (minVal,val-1)}
#             elif check == ">":
#                 positive = {result: (val+1,maxVal)}

#         elif 'str' in str(type(flow)):
#             return flow
#         else:
#             print("Bad:", flow)
            #    55167321008000
# code?:        183872022704000
# sample:       167409079868000
# too high:     874130835527971
# too low:       47951411392000

# find intersection?
intersections = []
i = 0
while i < len(allPoss):
    j = 0
    while j < len(allPoss):
        if not i == j:
            # get intersection?
            iPoss = allPoss[i]
            jPoss = allPoss[j]
            multiplier = 1
            for letter in "xmas":
                theMin = max(iPoss[letter][0], jPoss[letter][0])
                theMax = min(iPoss[letter][1], jPoss[letter][1])
                if theMax < theMin:
                    multiplier = 0
                    print("max < min", letter, iPoss[letter], jPoss[letter])
                else:
                    multiplier *= (theMax - theMin + 1)
            intersections.append(multiplier)
        j += 1
    i += 1

print("Collections:", sum(collect), collect)
print("Intersections", sum(intersections)/2, intersections)
print("Total:", sum(collect) - sum(intersections)/2)
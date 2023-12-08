groups = [[71, 2],
[43, 2],
[79, 5],
[53, 4],
[47, 4],
[61,3]]

vals = []
for g in groups:
    vals.append(g[1])


while len(set(vals)) > 1:
    
    smallest = min(vals)
    
    smallIndex = vals.index(smallest)
    multiplier = groups[smallIndex][0]

    vals[smallIndex] += multiplier

print(vals)

# multiplied = 36648605837
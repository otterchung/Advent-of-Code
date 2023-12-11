# groups = [[71, 2],
# [43, 2],
# [79, 5],
# [53, 4],
# [47, 4],
# [61,3]]



# vals = []
# for g in groups:
#     vals.append(g[1])

groups = [20093, 12169, 22357, 14999, 13301, 17263]
vals = [0,0,0,0,0,0]

j = 0
while len(set(vals)) > 1 or sum(vals) == 0:
    
    smallest = min(vals)
    
    smallIndex = vals.index(smallest)
    multiplier = groups[smallIndex]#[0]

    vals[smallIndex] += multiplier

    if j % 1000000 == 0:
        print(j)
    j += 1

print(vals)

# multiplied = 36648605837
# 71 m 53.1 s
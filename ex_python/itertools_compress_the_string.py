from  itertools import groupby
groups = []
uniquekeys = []
#data = input().strip()
data = s='1222311'
result1 = []
for k, g in groupby(data):
    groups.append(list(g))      # Store group iterator as a list
    uniquekeys.append(k)
result =[]
for i in range(len(uniquekeys)):
    result.append((len(groups[i]), int(uniquekeys[i])))
print(*result)

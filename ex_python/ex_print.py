from functools import reduce
c=[[1,2,3,4,5,6],[23,45,67,89,90],['a','d','df']]
s=reduce(lambda x,y:(x+y),c)
print(f"печать списка{s}\n")
for i in s:
    print(f"{i}")
print(f"печать списка{c}\n")
for i in c:
    for j in i:
        print(f"{j}")   


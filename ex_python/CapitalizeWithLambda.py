a="chris alan  chris alan"
from functools import reduce
l=a.split()
a=reduce(lambda i:a.replace(i,i.capitalize()),l)

print(a)

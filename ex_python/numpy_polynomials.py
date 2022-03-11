import numpy

a = list(map(float,input().strip().split() ))
x = float(input().strip())
y = 0
stepen = len(a)
for i in range(stepen):
    y+=a[i]*x**(stepen-i-1)
print(y)


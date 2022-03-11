import numpy
n,m = map(int,input().strip().split())
a = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
b = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
print(numpy.add(a,b))
print(numpy.subtract(a,b))
print(numpy.multiply(a,b))
print(a//b)
print(numpy.mod(a,b))
print(numpy.power(a,b))


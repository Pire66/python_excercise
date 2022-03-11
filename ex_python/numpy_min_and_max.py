import numpy

n,m = map(int,input().strip().split())
a = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
b = numpy.min(a, axis = 1)
print(numpy.max(b))



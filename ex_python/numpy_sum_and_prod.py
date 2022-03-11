import numpy

n,m = map(int,input().strip().split())
a = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
b = numpy.sum(a, axis = 0)
print(numpy.prod(b))



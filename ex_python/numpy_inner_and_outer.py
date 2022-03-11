import numpy

a = numpy.array(list(map(int,input().strip().split())) )
b = numpy.array(list(map(int,input().strip().split())) )
print(f'{numpy.inner(a,b)}\n{numpy.outer(a,b)}')


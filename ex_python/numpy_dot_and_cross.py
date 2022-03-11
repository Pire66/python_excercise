import numpy

n = int(input())
a = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
b = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
print(f'{numpy.dot(a,b)}')


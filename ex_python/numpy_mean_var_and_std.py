import numpy
numpy.set_printoptions(legacy='1.13')
n,m = map(int,input().strip().split())
a = numpy.array(list(list(map(int,input().strip().split())) for _ in range(n)))
print(f'{numpy.mean(a, axis = 1)}\n{numpy.var(a, axis = 0)}\n{round(numpy.std(a, axis = None),11)}')


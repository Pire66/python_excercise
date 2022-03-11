import numpy

numpy.set_printoptions(legacy='1.13')
a = numpy.array(list(map(float,input().strip().split() )))
print(f'{numpy.floor(a)}\n{numpy.ceil(a)}\n{numpy.rint(a)}')



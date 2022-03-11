import numpy
   
dimens = tuple(map(int,input().strip().split()))
print(numpy.zeros(dimens ,dtype = numpy.int32))
print(numpy.ones(dimens,dtype = numpy.int32))

import numpy
import numpy.linalg

n = int(input())
a = numpy.array(list(list(map(float,input().strip().split())) for _ in range(n)))
print(round(numpy.linalg.det(a),2))


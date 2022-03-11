import numpy as np

def arrays(arr):
    a = np.array(arr)
    return  np.reshape(a,(3,3))
    
arr = list(map(int,input().strip().split()))
result = arrays(arr)
print(result)

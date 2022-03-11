import numpy as np

def arrays(arr):
    a=np.array(arr, float)
    return  np.flip(a)
    
arr = input().strip().split(' ')
result = arrays(arr)
print(result)

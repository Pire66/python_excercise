import numpy as np
   
n,m = map(int,input().strip().split())
arr = np.array(list(list(map(int,input().strip().split())) for _ in range(n)))
#result = np.transpose(arr)
print(np.transpose(arr))
print(arr.flatten())

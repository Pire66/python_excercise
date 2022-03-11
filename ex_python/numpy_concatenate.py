import numpy as np
   
n,m,p = map(int,input().strip().split())
arr1 = np.array(list(list(map(int,input().strip().split())) for _ in range(n)))
arr2 = np.array(list(list(map(int,input().strip().split())) for _ in range(m)))
print(np.concatenate((arr1,arr2),axis = 0))

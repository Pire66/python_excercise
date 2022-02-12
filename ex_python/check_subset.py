def check_subset(set1, set2):
    n=len(string)
    for i in range(0,n,k):
        slicestr=string[i:i+k]
        shotstring=[]
        for j in list(slicestr):
            if j not in shotstring:
                shotstring.append(j)
        print(''.join(shotstring))
       
if __name__ == '__main__':
    k = int(input())
    for i in range(k):
        kset1, set1, kset2,set2 = int(input()),set(input().split()),int(input()),set(input().split())
        print(set1.issubset(set2))
   

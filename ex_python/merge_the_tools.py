def merge_the_tools(string, k):
    n=len(string)
    for i in range(0,n,k):
        slicestr=string[i:i+k]
        shotstring=[]
        for j in list(slicestr):
            if j not in shotstring:
                shotstring.append(j)
        print(''.join(shotstring))
       
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)

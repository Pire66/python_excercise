if __name__ == '__main__':
#    n = int(input())
    arr = map(int, input().split())
    n=5
#    arr=[2, 3, 6, 6, 5, 7,8]
#    s=set(arr)
    d=list(set(arr))
    print(d)
    d.sort()
    print(d)
    secondmax=d[-2]
    print(secondmax)

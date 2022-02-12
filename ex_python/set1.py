def average(array):
    s=set(array)
    kol_set=sum_set=0
    for i in s:
        sum_set+=i
        kol_set+=1
    return sum_set/kol_set

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

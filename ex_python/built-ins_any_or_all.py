if __name__ == '__main__':
    nm = input()
    arr = list(map(int, input().rstrip().split()))
    print(all(arr[i] >0 for i in range(len(arr))) and str(nm) == str(nm)[::-1])

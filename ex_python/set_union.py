if __name__ == '__main__':
    numer_set1 = int(input())
    set1 = set(map(int, input().split()))
    numer_set2 = int(input())
    set2 = set(map(int, input().split()))
    setunion = set1.union(set2)
    print(len(setunion))

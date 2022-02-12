if __name__ == '__main__':
    numer_set1 = int(input())
    set1 = set(map(int, input().split()))
    numer_set2 = int(input())
    set2 = set(map(int, input().split()))
    set3=sorted(set1.symmetric_difference(set2))
    for i in set3:
        print(i)

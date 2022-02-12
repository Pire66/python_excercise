if __name__ == '__main__':
    numer_set1 = int(input())
    set1 = set(map(int, input().split()))
    numer_set2 = int(input())
    set2 = set(map(int, input().split()))
    print(len(set1.symmetric_difference(set2)))

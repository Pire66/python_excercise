if __name__ == '__main__':
    from itertools import product
    listA = list(map(int, input().split()))
    listB = list(map(int, input().split()))    
    print(*list(product(listA,listB)))


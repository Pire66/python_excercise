if __name__ == '__main__':
    set1 = set(input().split())
    number_of_set = int(input())
    isstrict = True
    for i in range(number_of_set):
        subset = set(input().split())
        isstrict=isstrict and (set1.issuperset(subset))
    print(isstrict)
   

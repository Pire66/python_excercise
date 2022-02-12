if __name__ == '__main__':
    happiness = 0
    r_mysets = list(map(int, input().split()))
    myset = list(map(int, input().split()))
    setA = set(map(int, input().split()))
    setB = set(map(int, input().split()))
    for i in myset:
        if i in setA:
            happiness+=1
        if i in setB:
            happiness-=1
#    setHappy=myset.intersection(setA)
#    print(setHappy)
#    setNotHappy = myset.intersection(setB)
#    print(setNotHappy)
#    print(len(setHappy)-len(setNotHappy))
#    set3=sorted(set1.symmetric_difference(set2))
#    for i in set3:
#        print(i)
    print(happiness)

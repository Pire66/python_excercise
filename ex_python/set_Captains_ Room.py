if __name__ == '__main__':
    number_set = int(input())
    mystr = input().split()
    myset1 = set()
    myset2 = set()
    for i in mystr:
        if i in myset1:
           myset2.add(i)
        else:
           myset1.add(i)
    myset3 = myset1.difference(myset2)
    print(list(myset3)[0])

if __name__ == '__main__':
    number_set = int(input())
    myset = set(map(int, input().split()))
    number_command = int(input())
    for i in range(number_command):
        mycommand = input().split()
        myset2 = set(map(int, input().split()))
        if mycommand[0] == 'intersection_update':
            myset.intersection_update(myset2)
        elif mycommand[0] == 'update':
            myset.update(myset2)
        elif mycommand[0] == 'symmetric_difference_update':
            myset.symmetric_difference_update(myset2)
        elif mycommand[0] == 'difference_update':
            myset.difference_update(myset2)
    print(sum(myset))

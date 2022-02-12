if __name__ == '__main__':
    numer_set = int(input())
    myset = set(map(int, input().split()))
    number_command = int(input())
    for i in range(number_command):
        mycommand = input().split()
        if mycommand[0] == 'pop':
            myset.pop()
        elif mycommand[0] == 'remove':
            myset.remove(int(mycommand[1]))
        elif mycommand[0] == 'discard':
            myset.discard(int(mycommand[1]))
    print(sum(myset))

if __name__ == '__main__':
    t = int(input())
    sample_string = []
    for _ in range(t):
        sample_string.append(input())
    for i in sample_string:
        try:
           x = float(i)
           print(x)
           result = True if i.find('.')>0 else False
        except:
            result = False
        print(result)

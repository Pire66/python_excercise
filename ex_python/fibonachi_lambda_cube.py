cube =  lambda x: x**3

def fibonacci(n):
    if n == 0:
        arr = []
    elif n == 1:
        arr = [0]
    elif (n>=2 and n <=15):
        arr = [0,1]
        for i in range(2,n,1):
            nuber_fib = arr[-2] + arr[-1]
            arr.append(nuber_fib)
    else:
        arr = [] 
    return arr

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

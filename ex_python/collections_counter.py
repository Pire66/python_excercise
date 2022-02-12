from collections import Counter 
if __name__ == '__main__':
    X = int(input())
    list_shoe_size = list(map(int, input().split()))
    shoe_size = Counter(list_shoe_size)
    sum_money = 0
    N = int(input())
    for i in range(N):
        number_shoe_size,number_shoe_price = list(map(int, input().split()))
        if shoe_size.get(number_shoe_size,0)> 0:
            sum_money += number_shoe_price
            shoe_size[number_shoe_size] -= 1
print(sum_money)

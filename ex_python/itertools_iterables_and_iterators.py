from  itertools import combinations
len_data=int(input())
data = input().strip().split()
search = 'a'
k = int(input())
list_comb = list(combinations(data,k))
fr = 0
for i in list_comb:
    fr +=1 if search in i else 0
print(f'{round(fr/len(list_comb),4)}')

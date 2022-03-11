from  itertools import product
len_data,m = map(int,input().strip().split())
strings = list(list(map(int,input().strip().split()))[1:] for _ in range(len_data))
list_comb = product(*strings)
#result =[]
#for i in list_comb:
#    funct_summ_sq = 0
#    for j in i:
#        funct_summ_sq += j**2
#    result.append(funct_summ_sq%m)
result = map(lambda x: sum(i**2) for i in x)%m, list_comb)
print(max(result))

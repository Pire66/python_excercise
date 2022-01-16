# Напишите reducer, который объединяет элементы из множества A и B.
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

#     Sample Input:
#     1	A
#     2	A
#     2	B
#     3	B

#     Sample Output:
#     2



import sys

tempdict = dict()
result_list = []
for line in sys.stdin:
    el_set,marker_set = line.strip().split('\t')
    if tempdict.get(el_set):
        result_list.append(el_set)
    tempdict.update({el_set:marker_set})
for i in result_list:
    print(i)





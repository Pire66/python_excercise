# Напишите reducer, который объединяет элементы из множества A и B.
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

#     Sample Input:
#     1	A
#     2	A
#     2	B
#     3	B

#     Sample Output:
#     1
#     2
#     3


import sys

tempdict = dict()
for line in sys.stdin:
    el_set,marker_set = line.strip().split('\t')
    tempdict.update({el_set:marker_set})
for i in tempdict.keys():
    print(i)





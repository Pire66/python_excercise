# Напишите reducer, который делает вычитание элементов множества B из множества A.
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

#     Sample Input:
#     1	A
#     2	A
#     2	B
#     3	B

#     Sample Output:
#     1

import sys

tempdict = dict()
for line in sys.stdin:
    el_set,marker_set = line.strip().split('\t')
    list_marker_set = [marker_set]
    if tempdict.get(el_set):
        tmp_value = tempdict.get(el_set)
        list_marker_set.append(tmp_value)
    tempdict.update({el_set:list_marker_set})
temp_list_key = list(tempdict.keys())
for i in temp_list_key:
    if len(tempdict.get(i)) == 1 and tempdict.get(i)[0] == 'A':
        print(i)




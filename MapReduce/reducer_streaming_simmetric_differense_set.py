# Напишите reducer, который реализует симметричную разность множеств A и B(т.е. оставляет только те элементы, которые есть только в одном из множеств). 
# На вход в reducer приходят пары key / value, где key - элемент множества, value - маркер множества (A или B)

#     Sample Input:
#     1	A
#     2	A
#     2	B
#     3	B

#     Sample Output:
#     1
#     3

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
    if len(tempdict.get(i)) == 1 :
        print(i)




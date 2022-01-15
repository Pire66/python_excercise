# Mapper принимает на вход строку, содержащую значение и через табуляцию список групп, разделенных запятой
#     Sample Input:
# 1	a,b
# 2	a,d,e
# 1	b
# 3	a,b
#     Sample Output:

#     1,a	1
#     1,b	1
#     2,a	1
#     2,d	1
#     2,e	1
#     1,b	1
#     3,a	1
#     3,b	1


# это маппер
#for line in sys.stdin:
#    key,value = line.strip().split('\t')
#    dist = value.split(",")
#    for smalltoken in dist:
#        print(f'{key},{smalltoken}\t1')

# Reducer принимает на вход данные, созданные mapper из предыдущей шага.
# Sample Output:

# 1,a
# 1,b
# 2,a
# 2,d
# 2,e
# 3,a
# 3,b
import sys
#tempset=set()
#for line in sys.stdin:
#    key,value = line.strip().split('\t')
#    tempset.add(key)
#templist = list(tempset)
#templist.sort()
#for token in templist:
#    print(token)
#MAP_REDUCE STEP 2
#Mapper принимает на вход строку, содержащую значение и группу, разделенные запятой.
# Sample Input:

# 1,a
# 2,a
# 3,a
# 1,b
# 3,b
# 2,d
# 2,e
# Sample Output:

# a	1
# a	1
# a	1
# b	1
# b	1
# d	1
# e	1

#import sys

#for line in sys.stdin:
#    key,value = line.strip().split(',')
#    print(f'{value}\t1')

#REDUCER STEP 2
# Sample Input:
# 1	a
# 1	b
# 1	b
# 2	a
# 2	d
# 2	e
# 3	a
# 3	b
# Sample Output:
# a	3
# d	1
# b	2
# e	1

import sys
temp_array = {}
prev_key,prev_value = 0,None
for line in sys.stdin:
    key,value = line.strip().split('\t')
    if key == prev_key and value == prev_value:
        pass
    else:   
        prev_key,prev_value = key,value
        val = 1 if not temp_array.get(value) else (temp_array.get(value)+1)
        temp_array.update({value:val})
for temp_key in temp_array.keys():
    print(f'{temp_key}\t{temp_array.get(temp_key)})




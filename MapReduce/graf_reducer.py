# Реализуйте mapper в задаче поиска кратчайшего пути с помощью Hadoop Streaming.
# Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:
# Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
#Список исходящих вершин (через "," в фигурных скобках) 
#Sample Input:
# 1	0	{2,3,4}
# 10	INF	{}
# 10	INF	{}
# 2	1	{}
# 2	1	{5,6}
# 3	1	{}
# 3	1	{}
# 4	1	{}
# 4	1	{7,8}
# 5	2	{}
# 5	INF	{9,10}
# 6	2	{}
# 6	INF	{}
# 7	2	{}
# 7	INF	{}
# 8	2	{}
# 8	INF	{}
# 9	INF	{}
# 9	INF	{}

#Sample Output:
# 1	0	{2,3,4}
# 10	INF	{}
# 2	1	{5,6}
# 3	1	{}
# 4	1	{7,8}
# 5	2	{9,10}
# 6	2	{}
# 7	2	{}
# 8	2	{}
# 9	INF	{}

import sys
key_prev,value1_prev, value2_prev = (None, None, None)
for line in sys.stdin:
    key,value1, value2 = line.strip().split("\t")
    if key == key_prev:
        value1_prev = min(value1,value1_prev)
        value2_prev = min(value2,value2_prev)
    else:
        if key_prev != None:
            print(f'{key_prev}\t{value1_prev}\t{value2_prev}')
        key_prev,value1_prev, value2_prev = (key,value1, value2)
print(f'{key_prev}\t{value1_prev}\t{value2_prev}')   


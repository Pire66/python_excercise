# Реализуйте mapper в задаче поиска кратчайшего пути с помощью Hadoop Streaming.
# Входные и выходные данные: в качестве ключа идет номер вершины, значение состоит из двух полей, разделенных табуляцией:
# Минимальное расстояние до данной вершины (если его еще нет, то пишется INF)
#Список исходящих вершин (через "," в фигурных скобках) 
#Sample Input:
# 1	0	{2,3,4}
# 2	1	{5,6}
# 3	1	{}
# 4	1	{7,8}
# 5	INF	{9,10}
# 6	INF	{}
# 7	INF	{}
# 8	INF	{}
# 9	INF	{}
# 10	INF	{}

#Sample Output:
# 1	0	{2,3,4}
# 2	1	{}
# 3	1	{}
# 4	1	{}
# 2	1	{5,6}
# 5	2	{}
# 6	2	{}
# 3	1	{}
# 4	1	{7,8}
# 7	2	{}
# 8	2	{}
# 5	INF	{9,10}
# 9	INF	{}
# 10	INF	{}
# 6	INF	{}
# 7	INF	{}
# 8	INF	{}
# 9	INF	{}
# 10	INF	{}

import sys
for line in sys.stdin:
    key,value1, value2 = line.strip().split("\t")
    print(f'{key}\t{value1}\t{value2}')
    connect_vert = value2[1:-1].split(",")
    if  value2 != '{}':
        for vert in connect_vert:
            empty_set = '{}'
            try:
                new_value = int(value1)+1
            except:
                new_value = 'INF'
            print(f'{vert}\t{new_value}\t{empty_set}')


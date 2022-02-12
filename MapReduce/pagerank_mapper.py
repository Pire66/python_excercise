# Реализуйте mapper для алгоритма расчета PageRank с помощью Hadoop Streaming. 
# Входные и выходные данные: В качестве ключа идет номер вершины.
# Значение составное: через табуляцию записано значение PageRank (округленное до 3-го знака после запятой)
# и список смежных вершин (через "," в фигурных скобках).
#Sample Input:
# 1	0.200	{2,4}
# 2	0.200	{3,5}
# 3	0.200	{4}
# 4	0.200	{5}
# 5	0.200	{1,2,3}

#Sample Output:
# 1	0.200	{2,4}
# 2	0.100	{}
# 4	0.100	{}
# 2	0.200	{3,5}
# 3	0.100	{}
# 5	0.100	{}
# 3	0.200	{4}
# 4	0.200	{}
# 4	0.200	{5}
# 5	0.200	{}
# 5	0.200	{1,2,3}
# 1	0.067	{}
# 2	0.067	{}
# 3	0.067	{}

import sys
for line in sys.stdin:
    key,value1, value2 = line.strip().split("\t")
    print(f'{key}\t{value1}\t{value2}')
    connect_vert = value2[1:-1].split(",")
    if  value2 != '{}':
        weight = float(value1)/ len(connect_vert)
        empty_set = '{}'
        for vert in connect_vert:
             print(f'{vert}\t{weight:.3f}\t{empty_set}')


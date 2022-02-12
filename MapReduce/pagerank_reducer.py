# Реализуйте reducer для алгоритма расчета PageRank с помощью Hadoop Streaming.
# Используйте упрощенный алгоритм (без случайных переходов).
# Входные и выходные данные: В качестве ключа идет номер вершины.
# Значение составное: через табуляцию записано значение PageRank (округленное до 3-го знака после запятой)
# и список смежных вершин (через "," в фигурных скобках).
#Sample Input:
# 1	0.067	{}
# 1	0.200	{2,4}
# 2	0.067	{}
# 2	0.100	{}
# 2	0.200	{3,5}
# 3	0.067	{}
# 3	0.100	{}
# 3	0.200	{4}
# 4	0.100	{}
# 4	0.200	{}
# 4	0.200	{5}
# 5	0.100	{}
# 5	0.200	{}
# 5	0.200	{1,2,3}

#Sample Output:
# 1	0.067	{2,4}
# 2	0.167	{3,5}
# 3	0.167	{4}
# 4	0.300	{5}
# 5	0.300	{1,2,3}

import sys
key_prev,value1_prev, value2_prev = (None, 0.0, '{}')
for line in sys.stdin:
    key,value1, value2 = line.strip().split("\t")
    if key == key_prev:
        if value2 == '{}':
            value1_prev += float(value1)
        else:
            value2_prev = value2
    else:
        if key_prev != None:
            print(f'{key_prev}\t{value1_prev:.3f}\t{value2_prev}')
        key_prev, value2_prev = (key, value2)
        value1_prev = float(value1) if value2 == '{}' else 0.0
print(f'{key_prev}\t{value1_prev:.3f}\t{value2_prev}')   


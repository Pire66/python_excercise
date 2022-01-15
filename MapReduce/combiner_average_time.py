# Реализуйте Combiner в задаче подсчета среднего времени, проведенного пользователем на странице.
# Mapper пишет данные в виде key / value, где key - адрес страницы, value - пара чисел, разделенных ";".
# Первое - число секунд, проведенных пользователем на данной странице, второе равно 1.
import sys

(lastkey,summtime,kol) = (None,0,0)
for line in sys.stdin:
    (key,value) = line.strip().split("\t")
    valuetime = int(value.split(';')[0])
    if lastkey and lastkey != key:
        print(f'{lastkey}\t{summtime};{kol}')
        (lastkey,summtime,kol) = (key,valuetime,1)
    else:
        (lastkey,summtime,kol) = (key,summtime + valuetime,kol+1)
print(f'{lastkey}\t{summtime};{kol}')


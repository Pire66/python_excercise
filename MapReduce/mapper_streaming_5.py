# Реализуйте mapper для задачи Cross-Correlation, который для каждого кортежа создает stripe.
# Mapper принимает на вход кортежи - строки, состоящие из объектов, разделенных пробелом.
# Mapper пишет данные в виде key / value, где key - объект, value - соответствующий stripe (пример: a:1,b:2,c:3)
#     Sample Input:
# a b
# a b a c

#     Sample Output:
#     a	b:1
#     b	a:1
#     a	b:1,c:1
#     b	a:2,c:1
#     a	b:1,c:1
#     c	b:1,a:2

# это маппер
import sys

for line in sys.stdin:
    mtuple = tuple(line.strip().split(' '))
    for el_tuple1 in mtuple:
        ass_massive=dict()
        for el_tuple2 in mtuple:
            if el_tuple1 != el_tuple2:
                 val = 1 if not ass_massive.get(el_tuple2) else (ass_massive.get(el_tuple2)+1)
                 ass_massive.update({el_tuple2:val})
        stripe = ','.join(['{0}:{1}'.format(k,v) for (k,v) in ass_massive.items()])
        print(f'{el_tuple1}\t{stripe}')





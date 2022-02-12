#Реализуйте mapper ﻿второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
#Во входных данных ключом является слово, а значение состоит из номера документа и tf, разделенных табуляцией.
#Значение в выходных данных - это тройка: номер документа, tf и единица, разделенные ";".

#Sample Input:

# aut	1	4
# aut	2	2
# bene	2	1
# de	2	1
# mortuis	2	1
# nihil	1	1
# nihil	2	1
# Caesar	1	1

#Sample Output:

# aut	1;4;1
# aut	2;2;1
# bene	2;1;1
# de	2;1;1
# mortuis	2;1;1
# nihil	1;1;1
# nihil	2;1;1
# Caesar	1;1;1

#import sys
#for line in sys.stdin:
#    words = line.strip().split("\t")
#    print(f'{words[0]}\t{words[1]};{words[2]};1')

# Реализуйте reducer второй mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Входные данные: ключ - слово, значение - тройка: номер документа, tf слова в документе и 1 (разделены ';').
# Выходные данные: ключ - пара: слово, номер документа (разделены '#'),
# значение - пара: tf слова в документе, n - количество документов с данным словом (разделены табуляцией).

# Sample Input:
# aut	1;4;1
# aut	2;2;1
# bene	2;1;1
# de	2;1;1
# mortuis	2;1;1
# nihil	1;1;1
# nihil	2;1;1
# Caesar	1;1;1

# Sample Output:

# aut#1	4	2
# aut#2	2	2
# bene#2	1	1
# de#2	1	1
# mortuis#2	1	1
# nihil#1	1	2
# nihil#2	1	2
# Caesar#1	1	1

import sys

(lastkey,lastvalue) = (None,None)
tempdict = {}
for line in sys.stdin:
    (key,value) = line.strip().split("\t")
    list_value = value.split(";")
    lastkey = list(tempdict.keys())[0] if tempdict.keys() else ''
    if lastkey and lastkey != key:
        lastvalue = tempdict.get(lastkey)
        kol_doc = len(lastvalue)
        for el_dict in lastvalue:
            print(f'{lastkey}#{el_dict[0]}\t{el_dict[1]}\t{kol_doc}')
        tempdict.clear()
        tempdict = {key:[list_value]}
    else:
        out_value = tempdict.get(key) if tempdict.get(key) else []
        if len(out_value) > 0:
            out_value.append(list_value)
        else:
            out_value = [list_value]
        tempdict.update({key:out_value})
lastkey = key
lastvalue = tempdict.get(lastkey)
kol_doc = len(lastvalue)
for el_dict in lastvalue:
    print(f'{lastkey}#{el_dict[0]}\t{el_dict[1]}\t{kol_doc}')

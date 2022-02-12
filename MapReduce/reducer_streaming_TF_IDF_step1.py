#Реализуйте mapper первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.

# Формат входных данных следующий: каждая строка содержит номер документа и строку из него, разделенные ":".
# Ключ выходных данных является составным: он содержит слово документа и его номер, разделенные "#". 

# Слово в документе - последовательность символов (букв или цифр), не содержащая пробельных символов и знаков пунктуации.

#Sample Input:

#1:aut Caesar aut nihil
#1:aut aut
#2:de mortuis aut bene aut nihil
#Sample Output:

#aut#1	1
#Caesar#1	1
#aut#1	1
#nihil#1	1
#aut#1	1
#aut#1	1
#de#2	1
#mortuis#2	1
#aut#2	1
#bene#2	1
#aut#2	1
#nihil#2	1

# import sys
# import re
# text=''
# for line in sys.stdin:
#     text = line
#     text = re.compile('\w+').findall(line) 
#     doc_number = text[0]
#     text.remove(doc_number)
#     for i in text:
#         print(f'{i}#{doc_number}\t1')

# Реализуйте reducer первой mapreduce задачи для расчета TF-IDF с помощью Hadoop Streaming.
# Ключ входных данных составной: он содержит слово и номер документа через "#".
# Ключом в выходных данных является слово, а значение состоит из двух элементов, разделенных табуляцией:
# номер документа и tf (сколько раз данное слово встретилось в данном документе).

#Sample Output:
# aut	1	4
# aut	2	2
# bene	2	1
# de	2	1
# mortuis	2	1
# nihil	1	1
# nihil	2	1
# Caesar	1	1

import sys

tempdict = dict()
for line in sys.stdin:
    (key,value) = line.strip().split("\t")
    if tempdict.get(key):
        tempdict.update({key:tempdict.get(key)+int(value)}) 
    else:
        tempdict.update({key:int(value)})
for i in tempdict:
    k1,k2 = i.split("#")
    print(f'{k1}\t{k2}\t{tempdict.get(i)}')


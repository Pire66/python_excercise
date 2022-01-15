import sys

(lastkey,summ) = (None,0)
for line in sys.stdin:
    (key,value) = line.strip().split("\t")
    if lastkey and lastkey != key:
        print(lastkey+'\t' + str(summ))
        (lastkey,summ) = (key,int(value))
    else:
        (lastkey,summ) = (key,summ + int(value))
print(lastkey,summ)


import sys

(lastkey,summtime,kol) = (None,0,0)
for line in sys.stdin:
    (key,value) = line.strip().split("\t")
    if lastkey and lastkey != key:
        print(lastkey+'\t' + str(round(summtime / kol)))
        (lastkey,summtime,kol) = (key,int(value),1)
    else:
        (lastkey,summtime,kol) = (key,summtime + int(value),kol+1)
print(lastkey+'\t' + str(round(summtime / kol)))


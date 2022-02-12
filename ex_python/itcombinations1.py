from itertools import combinations
#word, k = input().split(" ")
#ks=int(k)
word='HACK'
ks=3
listword=list(word)
listword.sort()
for j in range(ks):
    listp=list(combinations(listword,j+1))
    for i in listp:
        print (''.join(i))


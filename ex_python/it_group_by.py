from itertools import combinations_with_replacement
#word, k = input().split(" ")
#ks=int(k)
word='HACK'
ks=2
listword=list(word)
listword.sort()
listp=list(combinations_with_replacement(listword,ks))
for i in listp:
     print (''.join(i))


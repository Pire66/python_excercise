from itertools import permutations
#word, k = input().split(" ")
word='HACK'
k=2
listp=sorted(list(permutations(word,k)))
for i in listp:
    print (''.join(i))


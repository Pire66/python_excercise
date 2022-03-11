#You are given an integer, N.
#Your task is to print an alphabet rangoli of size .
#(Rangoli is a form of Indian folk art based on creation of patterns.)
#For example,size 5
#
#--------e--------
#------e-d-e------
#----e-d-c-d-e----
#--e-d-c-b-c-d-e--
#e-d-c-b-a-b-c-d-e
#--e-d-c-b-c-d-e--
#----e-d-c-d-e----
#------e-d-e------
#--------e--------

def print_rangoli(size):
    defi = '-'
    alf_lat = 'abcdefghijklmnopqrstuvwxyz'
    deal_with = alf_lat[:size]
    width = size*4-3
    pict = ''
#Top Cone
    for i in range(size):
        pict = pict[:len(pict)//2+1]+defi+deal_with[size-(i+1)]+defi+pict[len(pict)//2:] if len(pict)>0 else deal_with[size-(i+1)]
        print(pict.center(width, defi))
#Bottom Cone
    for i in range(size-1):
        print(pict.center(width, defi))
        
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)


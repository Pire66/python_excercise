vert_size = 11
hor_size = 33
word = 'WELCOME'
#vert_size, hor_size = map(int,input().split())
half_vert_size = vert_size//2
half_hor_size = hor_size//2
defi = '-'
point = '.|.'

#Top Cone
for i in range(1,half_vert_size+1):
    print(defi*((hor_size-3*(2*i-1))//2)+point*(2*i-1)+ defi*((hor_size-3*(2*i-1))//2))

#WELCOME
print(defi*((hor_size-len(word))//2) + word + defi*((hor_size-len(word))//2))

#Bottom Cone
for i in range(1,half_vert_size+1):
    j= half_vert_size+1-i
    print(defi*((hor_size-3*(2*j-1))//2)+point*(2*j-1)+ defi*((hor_size-3*(2*j-1))//2))

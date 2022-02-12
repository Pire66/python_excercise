import textwrap
a='ABCDEFGHIJKLIMNOQRSTUVWXYZ'
v=4
s=textwrap.wrap(a,v)
l=''
for i in s:
    l+=i+'\n'
print(l)

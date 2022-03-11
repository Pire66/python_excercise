import re
regex_pattern = r'[QWRTYPSDFGHJKLZXCVBNM][AEIOU]{2,}[QWRTYPSDFGHJKLZXCVBNM]'
#a = list(map(lambda x:x.group(),re.finditer(regex_pattern,input(),flags = re.IGNORECASE)))
s = input()
i = 0
while len(s)>0:
    s = s[i:]
    a = re.search(regex_pattern,s,flags = re.IGNORECASE)
    if a:
        i = a.span()[1]-1
        print(a.group()[1:-1])
    else:
        if i==0:
            print('-1')
        break
    
    

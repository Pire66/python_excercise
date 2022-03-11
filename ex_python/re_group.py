import re
m = re.search(r"([0-9a-zA-Z])\1+", input())
try:
    print(m.group(1))
except:
    print('-1')
    

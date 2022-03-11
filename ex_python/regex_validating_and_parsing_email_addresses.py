regex_pattern = r'^[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}$'
import re
import email.utils
n = int(input()) 
all_text = list( input() for _ in range(n))
for i in all_text:
    a= re.match(regex_pattern,email.utils.parseaddr((i))[1])
    try:
        a.group() 
        print(i)
    except:
        pass
    
    

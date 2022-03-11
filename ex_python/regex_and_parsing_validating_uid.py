#Regex and Parsing Validating UID
import re

regex_patterns = [r"^[0-9A-Za-z]{10}$",
                  r"(.*[A-Z].*){2,}",    
                  r"(.*[0-9].*){3,}",    
                  r"^(?:([a-zA-Z0-9])(?!.*\1))*$"] 
t=int(input())
uids = [input().strip() for _ in range(t) ]
for uid in uids:
    sort_uid = ''.join(sorted(uid))
    result = True
    for regex_pattern in regex_patterns:
        result = result and re.match(regex_pattern,sort_uid)
    print('Valid' if result else 'Invalid')

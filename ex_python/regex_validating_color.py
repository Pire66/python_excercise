regex_pattern = r'(?<!^)#(?:[0-9A-Fa-f]{3}){1,2}'
import re
all_text = list( input() for _ in range(int(input())))
for i in all_text:
    a= re.findall(regex_pattern,i)
    if len(a) > 0:
        print('\n'.join(a))
    
    

regex_pattern = r"[789][0-9]{9}$"
import re
n = int(input()) 
all_text = list( input() for _ in range(n))
for i in all_text:
    print ('YES' if bool(re.match(regex_pattern, i)) else 'NO')
    
    

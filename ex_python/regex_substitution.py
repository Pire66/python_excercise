import re
n = int(input()) 
all_text = list( input() for _ in range(n))
regex_pattern = re.compile(r'(?<= )(\&\&|\|\|)(?= )')
for i in all_text:
    out_string = i
    searching_string = i.split('#')
    if len(searching_string) > 0:
        out_string = re.sub(regex_pattern, lambda x: "and" if x.group() == "&&" else "or", searching_string[0])
        out_string += ("#"+searching_string[1]) if len(searching_string) == 2 else ""
    print( out_string )
    
    

import re
s = input()
regex_pattern = re.compile(input())
start_search = 0
for i in range(len(s)):
    try:
        a = regex_pattern.search(s,start_search)
        start_search = a.start()+1
        print(f'({a.start()}, {a.end()-1})' )
        if start_search> len(s) or a.end()>=len(s):
            break 
    except:
        if i==0:
            print('(-1, -1)')
        break
    
    

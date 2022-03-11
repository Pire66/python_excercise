import re

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

regex_pattern = re.compile(r'(?<=\w)([^\w]+)(?=\w)')

matrix = []
for _ in range(n):
     matrix.append(list(input()))
check_string =''.join([matrix[i][j] for j in range(m) for i in range(n)])
neo_string = re.sub(regex_pattern,' ',check_string)
print(neo_string)

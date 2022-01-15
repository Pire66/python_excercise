# сокращение количества передаваемых пар ключ-значение за счет введения в маппер промежуточного массива
import sys
for line in sys.stdin:
    temp_array = {}
    for token  in line.strip().split(" "):
        val = 1 if not temp_array.get(token) else (val+1)
        temp_array.update({token:val})
    for temp_key in temp_array.keys():
        print(temp_key+'\t'+str(temp_array.get(temp_key)))


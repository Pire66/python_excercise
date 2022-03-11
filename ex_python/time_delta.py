import calendar
import math
import os
import random
import re
import sys
from datetime import datetime, date, time

# Complete the time_delta function below.
def time_delta(t1, t2):
    data_format = '%d %b %Y %H:%M:%S %z'
    tlist1 = datetime.strptime(t1[4:],data_format)
    tlist2 = datetime.strptime(t2[4:],data_format)
    return abs((tlist2-tlist1).days * 86400+(tlist2-tlist1).seconds)
    
if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()
        t2 = input()
        delta = time_delta(t1, t2)
#        fptr.write(delta + '\n')
        print(str(delta) + '\n')
#    fptr.close()


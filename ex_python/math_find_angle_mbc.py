# найти угол 
import math
a = int(input())
b = int(input())
c1d2 = math.hypot(a,b)/2
gamma = math.atan(a/b)
alfa = math.acos((c1d2-b*math.cos(gamma))/math.sqrt(b**2 + c1d2**2 - 2*b*c1d2*math.cos(gamma)))
beta = 180-math.degrees(gamma)-math.degrees(alfa)
print(f'{round(beta)}{chr(176)}')

import calendar

s= list(map(int, input().strip().split()))
print( list(calendar.day_name)[calendar.weekday(s[2],s[0],s[1])].upper() )

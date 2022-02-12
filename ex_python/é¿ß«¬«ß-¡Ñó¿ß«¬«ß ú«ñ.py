def is_leap(year):
    leap=False
    leap=(( year%4==0 and not year%100==0) or  (year%4==0 and year%100==0 and year%400==0))
    return leap

check_year=int(input())

print(is_leap(check_year))

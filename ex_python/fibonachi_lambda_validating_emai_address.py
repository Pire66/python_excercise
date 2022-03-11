def fun(s):
    temp_list = s.partition('@')
    result = False
    if len(temp_list) == 3:
        part1 = temp_list[0]
        result = (len(part1) > 0) and (part1 == ''.join(list(filter(lambda x: x.isalnum() or x in ('_','-'),part1))))
        temp_list2_3 = temp_list[2].rpartition('.')
        if len(temp_list2_3) == 3:
            part2 = temp_list2_3[0]
            result = result and (len(part2) > 0)and (part2 == ''.join(list(filter(lambda x: x.isalnum() ,part2))))
            part3 = temp_list2_3[2]
            result = result and (len(part3) >=1 and len(part3) <=3 ) and (part3 == ''.join(list(filter(lambda x: x.isalpha(),part3))))
        else:
            return False
    else:
        return False
    return result

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)

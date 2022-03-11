if __name__ == '__main__':
    string_for_sorting = input()
    arr = list(string_for_sorting)
    arr_lower_str = []
    arr_upper_str = []
    arr_odd_numb = []
    arr_even_numb = []
    for i in arr:
        if i.isalpha() and i.islower():
            arr_lower_str.append(i)
        elif i.isalpha() and i.isupper():
            arr_upper_str.append(i)           
        elif i.isdigit() and int(i)%2==0:
            arr_even_numb.append(i)           
        elif i.isdigit() and int(i)%2!=0:
           arr_odd_numb.append(i)
    arr_lower_str.sort()
    arr_upper_str.sort()
    arr_odd_numb.sort()
    arr_even_numb.sort()
    print(''.join(arr_lower_str+arr_upper_str+arr_odd_numb+arr_even_numb))

if __name__ == '__main__':
    string_expression = input()
    result = eval(string_expression)
    if  string_expression[:5] != 'print':
        print(result)

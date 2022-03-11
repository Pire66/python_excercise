from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        if data!= '\n':
            print(f'>>> Data\n{data}')
        
    def handle_comment(self, data):
        if data!= '\n':
            number_string=data.split('\n')
            if len(number_string) == 1:
                print(f'>>> Single-line Comment\n{data}')
            else:
                print(f'>>> Multi-line Comment\n{data}')
          
  
html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

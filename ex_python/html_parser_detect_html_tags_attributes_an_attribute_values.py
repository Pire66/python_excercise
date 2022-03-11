from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_data(self, data):
        pass
        
    def handle_comment(self, data):
        pass
                
    def handle_starttag(self, tag, attrs):
        print(tag)
        if  attrs:
            for attr, val in attrs:
                print('->', attr, '>', val) 

    def handle_endtag(self, tag):
        pass

    def handle_startendtag(self, tag, attrs):
        print (tag)
        if attrs:
            for attr, val in attrs:
                print('->', attr, '>', val) 


html = ""       
for i in range(int(input())):
    html += input().rstrip()
    html += '\n'
    
parser = MyHTMLParser()
parser.feed(html)
parser.close()

from html.parser import HTMLParser

class SimpleHTMLParser(HTMLParser):

    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
#        self.value(attrs)
        if attrs:
            [print('->', attr, '>', val) for attr, val in attrs]

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
#        self.value(attrs)
        if attrs:
            [print('->', attr, '>', val) for attr, val in attrs]

#    def value(self, attrs = None):
#        if attrs:
#            [print('->', attr, '>', val) for attr, val in attrs]

html_page = '\n'.join([input() for x in range(int(input()))])
parser = SimpleHTMLParser()
parser.feed(html_page)

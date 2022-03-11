import sys
import xml.etree.ElementTree as etree

maxdepth = 0
def depth(elem, level):
    global maxdepth
    if len(elem)>0:
        level +=1
        maxdepth = (maxdepth + 1) if level >= maxdepth else maxdepth
        for child in elem:
            depth(child, level)

    
if __name__ == '__main__':
    n = int(input())
    xml = ""
    for i in range(n):
        xml =  xml + input() + "\n"
    tree = etree.ElementTree(etree.fromstring(xml))
    depth(tree.getroot(), -1)
    print(maxdepth)

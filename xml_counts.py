import urllib.request
import xml.etree.ElementTree as ET


g = input("Enter the url : ")
response = urllib.request.urlopen(g)
html = response.read()

tree = ET.fromstring(html)

counts = tree.findall('.//count')

c=0
for count in counts:
    tt = int(count.text)
    c=c+tt
print(c)

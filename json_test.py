import json
import urllib.request


g = input("Enter the url : ")
response = urllib.request.urlopen(g)
html = response.read()

info = json.loads(html)
comments = info['comments']
c=0

for item in comments:
    c=c+ii.get(('count'),0)
print(c)

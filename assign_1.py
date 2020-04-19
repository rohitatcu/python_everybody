import re

f=open('regex_sum_450065.txt')
text = f.read()

numbers = re.findall('[0-9]+', text)

s = 0
for i in numbers:
    s=s+int(i)

print s

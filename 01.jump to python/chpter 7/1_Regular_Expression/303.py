import re

p=re.compile("[a-z]+") # 0또는 1만 적용이된다.
a=p.match('python')
print(a)
# a=p.search('cat')
# print(a)
# a=p.findall('caat')
# print(a)
# a=p.finditer('cats')
# print(a)

if a:
    print("Match found :", a.group()) # 문자사이에 , 는 공백문자
else:
    print("No match")
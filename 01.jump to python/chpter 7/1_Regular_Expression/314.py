import re
p = re.compile('Crow|Servo')
m = p.match('NoThing')
print(m)
m = p.match('Crow')
print(m)
m = p.match('Servo')
print(m)
m = p.match('CrowServo')
print(m)


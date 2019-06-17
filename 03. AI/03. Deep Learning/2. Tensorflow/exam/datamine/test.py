with open("SW_Episode4.txt",'r') as f:
    c=f.readlines()

i=0
e=[]
for b in c:
    i+=1

    d='"'+str(i)+'"'
    b=b.replace(d,"")
    b = b.replace(',', "")
    b=b.replace('" "',",")
    b=b.replace('"',"")
    e.append(b)
e=''.join(e)
print(e)
with open("sw_ep",'w') as f:
    f.write(e)
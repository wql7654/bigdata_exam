denominator = int(input("분모를 입력하세요:"))

try:
    f=open("새파일.txt", 'r')
    result = 4/denominator
    
except FileNotFoundError as e:
    print(e)

print("Finally 블록 수행")
f.close()

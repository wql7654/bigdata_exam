# 입력(parameter)이 있고, 출력(return) 이 없는 함수

def sum_type(num1,num2):
    # 함수 정의(define)
    num1=num1+10000
    num2=num2+10000
    print("num1+num2="+str(int(num1)+int(num2)))

# 함수 호출시 사용되는 입력(parameter) 는 호출되기 전에 준비(결정)한다.
num1, num2= input("두 수를 입력하세요").split()
num1=int(num1)
num2=int(num2)
sum_type(num1,num2)



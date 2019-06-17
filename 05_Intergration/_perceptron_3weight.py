def AND(x1,x2):
    w1,w2 = 0.5,0.5
    b = -0.7 # 편향값이 들어오면 세타값이 없어진다.
    tmp =x1*w1+x2*w2 +b

    if tmp <= 0: # 세타값이 없어지면 이렇게 0을 집어넣는다.
        return 0
    else:
        return 1

print(AND(0,0))
print(AND(1,0))
print(AND(0,1))
print(AND(1,1))
#2번째 예제와 p51~보면 이해 도움
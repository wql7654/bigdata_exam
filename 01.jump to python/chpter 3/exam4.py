# coding: cp949

age_str=input("���̸� �Է��ϼ���:")
age=int(age_str)
tap=0
if age>=0 and age<=3:
    money='����'
    vip='����'
elif age>3 and age<=13:
    money=2000
    vip='���'
elif age>13 and age<=18:
    money=3000
    vip='û�ҳ�'
elif age>20 and age<=65:
    money=5000
    vip='����'
elif age>65:
    money='����'
    vip='����'
else:
    print("�ٽ��Է��ϼ���")
    exit()

if money=='����':
    print("������ %s ����̸� ����� %s �Դϴ�." %(vip,money))
    print("�����մϴ� ��ſ� �ð� ��������")
    exit()
elif money!='����':
    print("������ %s ����̸� ����� %s�� �Դϴ�." %(vip,money))
    money_type_str=input("��� ������ �����ϼ���.(1:����, 2:���� ���� �ſ� ī��):")
    money_type=int(money_type_str)
    if(money_type==1):
        print("����� �Է��ϼ���")
        money_str=input()
        money_input=int(money_str)
        if money_input==money:
            print("�����մϴ�. Ƽ���� �����մϴ�.")
        elif money_input>=money:
            print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s���� ��ȯ�մϴ�."%(money_input-money))
        elif money_input<money:
            print("�ݾ��� �����մϴ� �����ѱݾ� %s���� ��ȯ�մϴ�."%(money_input))
    elif(money_type==2):
        if(age<=65 and age>=60):
            money_card=(((money*90)/100)*95)/100
        else:
            money_card=(money*90)/100
        print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%money_card)
    else:
        exit()
    


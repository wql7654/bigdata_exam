# coding: cp949

print("���̸� �Է��ϼ���:")
year_str=input()
year=int(year_str)
tap=0
if year>=0 and year<=3:
    money='����'
    vip=1
elif year>=4 and year<=13:
    money='2000��'
    vip=2
elif year>=14 and year<=18:
    money='3000��'
    vip=3
elif year>=19 and year<=65:
    money='5000��'
    vip=4
elif year>=66:
    money='����'
    vip=5
else:
    tap=1
    print("�ٽ��Է��ϼ���")

if tap!=1:
    print("������ %s ����̸� ����� %s �Դϴ�." %(vip,money))


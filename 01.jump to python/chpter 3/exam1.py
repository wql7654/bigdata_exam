# coding: cp949

print("���̸� �Է��ϼ���")
year_str=input()
year=int(year_str)

if year>=0 and year<=3:
    print("����� ���� �Դϴ�")
elif year>=4 and year<=13:
    print("����� 2000�� �Դϴ�")
elif year>=14 and year<=18:
    print("����� 3000�� �Դϴ�")
elif year>=19 and year<=65:
    print("����� 5000�� �Դϴ�")
elif year>=66:
    print("����� ���� �Դϴ�")




# coding: cp949
feel="ȣ��"
#feel = ""
hit_on_count=0

while feel:
    hit_on_count=hit_on_count+1
    print("%s�� ����Ʈ ��û�մϴ�."%hit_on_count)
    if hit_on_count==10:
        print("����� ���� �ٰ� �Գ׿�.")
        break
    feel = input("���� �׳࿡ ���� ����� ������ �����?")
    if(feel == "��ȣ��"):
        break

    




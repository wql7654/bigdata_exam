# coding: cp949

ticket_count=0
free_ticket=3
sale_ticket=5
while True:
   age_str=input("���̸� �Է��ϼ���:")
   age=int(age_str)
   
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
       continue

   if money=='����':
       print("������ %s ����̸� ����� %s �Դϴ�." %(vip,money))
       print("�����մϴ� ��ſ� �ð� ��������")
       #exit()
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
               ticket_count+=1
           elif money_input>=money:
               print("�����մϴ�. Ƽ���� �����ϰ� �Ž����� %s���� ��ȯ�մϴ�."%(money_input-money))
               ticket_count+=1
           elif money_input<money:
               print("�ݾ��� �����մϴ� �����ѱݾ� %s���� ��ȯ�մϴ�."%(money_input))
               continue
				
       elif(money_type==2):
           if(age<=65 and age>=60):
               money_card=(((money*90)/100)*95)/100
           else:
               money_card=(money*90)/100
           print("%d�� ���� �Ǿ����ϴ�. Ƽ���� �����մϴ�."%money_card)
           ticket_count+=1

       if(ticket_count%8==0 and free_ticket>0):
           free_ticket-=1
           ticket_count+=1
           print("�����մϴ�. 1�ֳ� �̺�Ʈ�� ��÷�Ǿ����ϴ� ���� ����Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%free_ticket)
       elif(ticket_count%5==0  and sale_ticket>0):
           sale_ticket-=1
           ticket_count+=1
           print("�����մϴ�. ����ȸ���� ���� �̺�Ʈ�� ��÷�Ǽ̽��ϴ�. ���� ȸ�� ���� Ƽ���� �����մϴ�. �ܿ� ����Ƽ�� %d��"%sale_ticket)
       
   # modify1
   # modify2

#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019.11.14
"""

import random

# 0 - ʯͷ
# 1 - ʷ����
# 2 - ֽ
# 3 - ����
# 4 - ����

print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
def name_to_number(choice_name):
	if choice_name=="ʯͷ":
		return 0
	elif choice_name=="ʷ����":
		return 1
	elif choice_name=="ֽ":
		return 2
	elif choice_name=="����":
		return 3
	elif choice_name=="����":
		return 4
	else:
		return 5
player_choice_number=name_to_number(choice_name)

comp_number=random.randrange(0,5)
def number_to_name(comp_number):
	if comp_number==0:
		print("�������ѡ��Ϊ��ʯͷ")
	elif comp_number==1:
		print("�������ѡ��Ϊ��ʷ����")
	elif comp_number==2:
		print("�������ѡ��Ϊ��ֽ")
	elif comp_number==3:
	    print("�������ѡ��Ϊ������")
	elif comp_number==4:
		print("�������ѡ��Ϊ������")
if player_choice_number==5:
	print("Error: No Correct Name")
else:
	number_to_name(comp_number)

def rpsls(player_choice):
	if player_choice_number==comp_number:
		print("���ͼ��������һ����")
	elif (player_choice_number==0 and comp_number==3) or (player_choice_number==0 and comp_number==4):
		print("��Ӯ��")
	elif (player_choice_number==1 and comp_number==0) or (player_choice_number==1 and comp_number==4):
		print("��Ӯ��")
	elif (player_choice_number==2 and comp_number==0) or (player_choice_number==2 and comp_number==1):
		print("��Ӯ��")
	elif (player_choice_number==3 and comp_number==1) or (player_choice_number==3 and comp_number==2):
		print("��Ӯ��")
	elif (player_choice_number==4 and comp_number==2) or (player_choice_number==4 and comp_number==3):
		print("��Ӯ��")
	elif (player_choice_number==0 and comp_number==1) or (player_choice_number==0 and comp_number==2):
		print("�����Ӯ��")
	elif (player_choice_number==1 and comp_number==3) or (player_choice_number==1 and comp_number==2):
		print("�����Ӯ��")
	elif (player_choice_number==2 and comp_number==3) or (player_choice_number==2 and comp_number==4):
		print("�����Ӯ��")
	elif (player_choice_number==3 and comp_number==0) or (player_choice_number==3 and comp_number==4):
		print("�����Ӯ��")
	elif (player_choice_number==4 and comp_number==0) or (player_choice_number==4 and comp_number==1):
		print("�����Ӯ��")

rpsls(choice_name)

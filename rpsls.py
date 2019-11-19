#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：漆宇翔
日期：2019.11.14
"""

import random

# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
def name_to_number(choice_name):
	if choice_name=="石头":
		return 0
	elif choice_name=="史波克":
		return 1
	elif choice_name=="纸":
		return 2
	elif choice_name=="蜥蜴":
		return 3
	elif choice_name=="剪刀":
		return 4
	else:
		return 5
player_choice_number=name_to_number(choice_name)

comp_number=random.randrange(0,5)
def number_to_name(comp_number):
	if comp_number==0:
		print("计算机的选择为：石头")
	elif comp_number==1:
		print("计算机的选择为：史波克")
	elif comp_number==2:
		print("计算机的选择为：纸")
	elif comp_number==3:
	    print("计算机的选择为：蜥蜴")
	elif comp_number==4:
		print("计算机的选择为：剪刀")
if player_choice_number==5:
	print("Error: No Correct Name")
else:
	number_to_name(comp_number)

def rpsls(player_choice):
	if player_choice_number==comp_number:
		print("您和计算机出的一样呢")
	elif (player_choice_number==0 and comp_number==3) or (player_choice_number==0 and comp_number==4):
		print("您赢了")
	elif (player_choice_number==1 and comp_number==0) or (player_choice_number==1 and comp_number==4):
		print("您赢了")
	elif (player_choice_number==2 and comp_number==0) or (player_choice_number==2 and comp_number==1):
		print("您赢了")
	elif (player_choice_number==3 and comp_number==1) or (player_choice_number==3 and comp_number==2):
		print("您赢了")
	elif (player_choice_number==4 and comp_number==2) or (player_choice_number==4 and comp_number==3):
		print("您赢了")
	elif (player_choice_number==0 and comp_number==1) or (player_choice_number==0 and comp_number==2):
		print("计算机赢了")
	elif (player_choice_number==1 and comp_number==3) or (player_choice_number==1 and comp_number==2):
		print("计算机赢了")
	elif (player_choice_number==2 and comp_number==3) or (player_choice_number==2 and comp_number==4):
		print("计算机赢了")
	elif (player_choice_number==3 and comp_number==0) or (player_choice_number==3 and comp_number==4):
		print("计算机赢了")
	elif (player_choice_number==4 and comp_number==0) or (player_choice_number==4 and comp_number==1):
		print("计算机赢了")

rpsls(choice_name)

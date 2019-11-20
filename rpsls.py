#coding:gbk
"""
��һ��С��Ŀ��Rock-paper-scissors-lizard-Spock
���ߣ�������
���ڣ�2019.11.20
"""

import random


# 0 - ʯͷ
# 1 - ʷ����
# 2 - ��
# 3 - ����
# 4 - ����

# ����Ϊ�����Ϸ����Ҫ�õ����Զ��庯��


def name_to_number(name):
    if name=="ʯͷ":
        return 0
    elif name=="ʷ����":
        name=1
    elif name=="��":
        name=2
    elif name=="����":
        name=3
    elif name=="����":
        name=4
    else:
	    return("Error: No Correct Name")    				


def number_to_name(number):
    """
    ������ (0, 1, 2, 3, or 4)��Ӧ����Ϸ�Ĳ�ͬ����
    """
    if number==0:
        return("ʯͷ")
    elif number==1:
        return("ʷ����")	
    elif number==2:
        return("��")	
    elif number==3:
        return("����")	
    elif number==4:
        return("����")	
 	
		


def rpsls(player_choice):
    """
    �û�����������һ��ѡ�񣬸���RPSLS��Ϸ��������Ļ�������Ӧ�Ľ��

    """
    player_choice_number=name_to_number(player_choice)
    print("����ѡ��Ϊ:%s"%player_choice)
    comp_number=random.randint(0,4)
    print("������ѡ��Ϊ:%s"%number_to_name(comp_number))
    if comp_number==player_choice_number:
        return("���ͼ��������һ����")
    elif player_choice_number==("Error: No Correct Name"):
        return("Error: No Correct Name")    
    elif player_choice_number==0 and (int(comp_number) in [3,4]):
        return("��Ӯ��")
    elif player_choice_number==1 and (int(comp_number) in [0,4]):	
        return("��Ӯ��")
    elif player_choice_number==2 and (int(comp_number) in [0,1]):	
        return("��Ӯ��")	
    elif player_choice_number==3 and (int(comp_number) in [1,2]):	
	    return("��Ӯ��")
    elif player_choice_number==4 and (int(comp_number) in [2,3]):	
        return("��Ӯ��")
    else:
        return("����Ӯ��")
    			


# �Գ�����в���
print("��ӭʹ��RPSLS��Ϸ")
print("----------------")
print("����������ѡ��:")
choice_name=input()
print(rpsls(choice_name))




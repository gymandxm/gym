#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：管佑名
日期：2019.11.20
"""

import random


# 0 - 石头
# 1 - 史波克
# 2 - 布
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数


def name_to_number(name):
    if name=="石头":
        return 0
    elif name=="史波克":
        name=1
    elif name=="布":
        name=2
    elif name=="蜥蜴":
        name=3
    elif name=="剪刀":
        name=4
    else:
	    return("Error: No Correct Name")    				


def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """
    if number==0:
        return("石头")
    elif number==1:
        return("史波克")	
    elif number==2:
        return("布")	
    elif number==3:
        return("蜥蜴")	
    elif number==4:
        return("剪刀")	
 	
		


def rpsls(player_choice):
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """
    player_choice_number=name_to_number(player_choice)
    print("您的选择为:%s"%player_choice)
    comp_number=random.randint(0,4)
    print("机器的选择为:%s"%number_to_name(comp_number))
    if comp_number==player_choice_number:
        return("您和计算机出的一样呢")
    elif player_choice_number==("Error: No Correct Name"):
        return("Error: No Correct Name")    
    elif player_choice_number==0 and (int(comp_number) in [3,4]):
        return("您赢了")
    elif player_choice_number==1 and (int(comp_number) in [0,4]):	
        return("您赢了")
    elif player_choice_number==2 and (int(comp_number) in [0,1]):	
        return("您赢了")	
    elif player_choice_number==3 and (int(comp_number) in [1,2]):	
	    return("您赢了")
    elif player_choice_number==4 and (int(comp_number) in [2,3]):	
        return("您赢了")
    else:
        return("机器赢了")
    			


# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input()
print(rpsls(choice_name))




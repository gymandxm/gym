#coding:gbk
'''
����Python��Gelphi�ġ����������Ľֵ��������ϵͼ�׹���
����:������
'''

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

 

names = {}#�����ֵ�
relationships = {}#��ϵ�ֵ�
lines = []#ÿ�������ϵ��ϵ


jieba.load_userdict('figure_dict.txt')#���������ֵ�
i=codecs.open("���������Ľֵ�.txt", "r", "gbk")
for line in i.readlines():
	y = pseg.cut(line)
	lines.append([])#ÿ��һ�ξ���Ӹö�����
	for x in y:
		if x.flag != "nr" or len(x.word) < 2:#�ж��Ƿ�������
			continue
		lines[-1].append(x.word)
		if names.get(x.word) is None:
			names[x.word] = 0
			relationships[x.word] = {}
		names[x.word] += 1#�����������ֵĴ���

 
#�ж�ÿһ�����������˳��ֵĴ���
for line in lines:
	for one in line:
		for two in line:
			if one == two:
				continue
			if relationships[one].get(two) is None:#δ�������½�
				relationships[one][two]= 1
			else:
				relationships[one][two] = relationships[one][two]+ 1#���ִ�����һ
#������д��csv�ı���������Gelphi����
j=codecs.open("point.csv", "w", "gbk")
j.write("Name Label Weight\r\n")
for name, times in names.items():
	j.write(name + " " + name + " " + str(times) + "\r\n")
k=codecs.open("side.csv", "w", "gbk")
k.write("Source Relationship Weight\r\n")
for name,edges in relationships.items():
	for v, n in edges.items():
		if n > 3:
			k.write(name + " " + v + " " + str(n) + "\r\n")




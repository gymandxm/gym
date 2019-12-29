#coding:gbk
'''
基于Python和Gelphi的《黎明破晓的街道》人物关系图谱构建
作者:管佑名
'''

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

 

names = {}#名字字典
relationships = {}#关系字典
lines = []#每段人物关系关系


jieba.load_userdict('figure_dict.txt')#加载人物字典
i=codecs.open("黎明破晓的街道.txt", "r", "gbk")
for line in i.readlines():
	y = pseg.cut(line)
	lines.append([])#每读一段就添加该段人物
	for x in y:
		if x.flag != "nr" or len(x.word) < 2:#判断是否是人名
			continue
		lines[-1].append(x.word)
		if names.get(x.word) is None:
			names[x.word] = 0
			relationships[x.word] = {}
		names[x.word] += 1#计算人名出现的次数

 
#判断每一段任意两个人出现的次数
for line in lines:
	for one in line:
		for two in line:
			if one == two:
				continue
			if relationships[one].get(two) is None:#未出现则新建
				relationships[one][two]= 1
			else:
				relationships[one][two] = relationships[one][two]+ 1#出现次数加一
#将数据写入csv文本，便于与Gelphi引用
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




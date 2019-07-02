#encoding=gbk
from snownlp import SnowNLP
import re
import random
import os
import jieba
import jieba.analyse
import json
import pygal
import wordcloud
from collections import Counter


stopwords_=['��֪','����','����','����','����','����','�α�','����','����','��ʱ','˭֪','����','���','�δ�','����','����']
screen_words=['��','��','��','��','��','��','ȥ','Ϊ','��','��','��','��','˭','��','��','��','��','��','��','��','��',
	'��','��','��','��','��','ʱ','-','��','��','��','��','��','��','һ','ȴ','��','��','��','֮','��','��','��','��',
	'��','δ','��','�δ�','��','��','��֪','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��','��',
	'��','��','·','����','��','��','��','ͬ','ǰ','}','��','{','��','��','��','����','��','��',']','[','��','˵','��',
	'��','����','��','Ӧ','֪','��','��','��','����','��','��','��','��','��','Ҳ','��','��','��','��','����','��','��',
	'��','��','��','��','��','��','��','��','ʹ','��','��','���','�v','��','��','��','��','��','��','��','��','��',' ','��'
	,'��','\n','��','��','/','��','��','��','��','��','��','Ҫ','(',')','��','ֻ','��','��']

pos=0 #ʫ��Ļ�������
l_pos=0 #��ʵĻ�������
l=0 #ѡȡ��ʫ������
l_l=1 #ѡȡ�ĸ������
def files_combination(file_path): #����һ���ļ���������ʫ���ļ�  
    words=''  
    i=1  
    for file_name in os.listdir(file_path):  
        print(i)  
        i=i+1  
        hh=words_combination(file_path+'\\'+file_name)  
        words=words+hh  
    return words  
  
def words_emotion(file_name):#���ļ��������ȡ��ʫ��  
    sentence_combination=''  
    global pos #ʹ��ȫ�ֱ���  
    global l  
    with open(file_name,'r',encoding='UTF-8') as f:  
        shiji=json.load(f)  
        for zidian in shiji:  
            shi=zidian["paragraphs"]  
            for sentence in shi:  
                a=random.randint(0,100)#���������  
                if a==30:#���������ѡȡԭ�ı��İٷ�֮һ  
                    s = SnowNLP(sentence)#������з���  
                    pos=pos+s.sentiments  
                    l=l+1#ͳ��ѡȡ������  
                    sentence_combination=sentence+sentence_combination  
    return sentence_combination  
def lyric_emotion():#�Ը�ʽ�����з���
	global l_l
	global l_pos
	lyric=''
	for file_name in os.listdir(r'\lyric'):
		with open(r'lyric\\' + file_name) as lrc:
			for line in lrc:
				words = re.sub(r'\[.+\]', '', line) 
				if '��' not in words:
					l_l=l_l+1
					s=SnowNLP(words)
					l_pos=l_pos+s.sentiments
					lyric=lyric+words

def gulong():#����С˵�ķ���
	p1=0
	l1=0
	for file_name in os.listdir(r'ziliao\������ȫ�� 76����ȫ(TXT)���ߣ�����'):
		with open(r'ziliao\������ȫ�� 76����ȫ(TXT)���ߣ�����\\' + file_name) as f2:
			p2=0
			l2=0
			for line in f2:
				a=random.randint(0,100)#���������  
				if a<30:
					l2=l2+1
					s=SnowNLP(line)
					p2=p2+s.sentiments
			p2=p2/l2
			print(file_name+' '+str(p2))
	
def create_cloud(words,stop_words,name):  
	cut_words = jieba.cut(words)       #���ɴ���ͼƬ
	word_co=','.join(cut_words)
	w=wordcloud.WordCloud(font_path=r'C:\Windows\Fonts\STKAITI.TTF',
		background_color="white",width=2000,height=1500,stopwords=stopwords_,
		max_words=300,max_font_size=225)
	w.generate(word_co)
	file_path=name+'_picture.png'
	w.to_file(file_path)
	
def xuezhong():  #ѩ�к����еķ���
	words=''
	with open(r'ziliao\ѩ�к�����.txt') as f2:
		p2=0
		l2=0
		for line in f2:
			a=random.randint(0,100)#���������  
			if a<10:
				l2=l2+1
				s=SnowNLP(line)
				p2=p2+s.sentiments
				print(a)
				words=words+line
		p2=p2/l2
		print(str(p2))
	return words

if __name__=='__main__':
	
	words=xuezhong()
	create_cloud(words,stopwords_,'xuezong')
	


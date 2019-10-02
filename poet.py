# coding: utf-8
from numpy.random import randint 
from numpy.random import choice
words = '''
西瓜
花花
傻眼
貓咪
是在
哈囉
我
我的
妳
妳的
心
溫柔
日子
雨
風
天空
雲
等待
哭泣
戀愛
相遇
分離
忘記
心醉
驀然
吹過
思念
靈魂
停止
亂數
排列組合
笑死
地板
驗收
迎新
舞展'''
phrase = words.split('\n')
n = randint(3,6) #3~5句

for i in range(n):
    k = randint(2,6)
    egg = choice(phrase, k)
    ham = ' '.join(egg)
    print(ham)

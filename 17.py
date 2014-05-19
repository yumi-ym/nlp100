# coding:utf-8

import sys
import re

# 人名らしき文字列（さん、氏、ちゃんを含む表現）を抽出する
p = re.compile(u'[一-龠ぁ-ゞァ-ヾ]+?(さん|氏|ちゃん)')

for a in sys.stdin.readlines():
	q = unicode(a, 'utf-8')
	searched = p.search(q)
	if searched:
		print searched.group()
		
	
		
		
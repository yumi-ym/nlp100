# coding:utf-8

import sys
import re

# 絵文字らしき文字列（丸括弧で囲まれた記号）を抽出する
p = re.compile(u'\([^一-龠ぁ-ゞァ-ヾ]+\W+\)')

for a in sys.stdin.readlines():
	q = unicode(a, 'utf-8')
	searched = p.search(q)
	if searched:
		print searched.group()
		
	
		
		
		
# coding:utf-8

import sys
import re

# 左側に漢字、右側に丸括弧で囲まれたアルファベット大文字の文字列を抽出する
p = re.compile(u'[一-龠]+?\([A-Z]+\)')

for a in sys.stdin.readlines():
	q = unicode(a, 'utf-8')
	searched = p.search(q)
	
	if searched:
		s = searched.group()
		
		# 文字列をタブで区切り、漢字とアルファベット大文字を並べる
		t = s.replace('(', '\t').rstrip(')')
		print t
		
		
		
		
		
		
		
		
		
		
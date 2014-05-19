# coding:utf-8

import sys
import re

# 郵便番号・県名・市町村名の３要素を含むツイートを抽出する（郵便番号、県名、市町村名の順に表示する）
p = re.compile(u'([1-9][0-9][0-9]-[0-9]{4})([一-龠]+?(都|道|府|県))([一-龠ぁ-ゞァ-ヾ]+(市|町|村))')

for a in sys.stdin.readlines():
	q = unicode(a, 'utf-8')
	searched = p.search(q)
	
	if searched:
		t = searched.group(1,2,4)
		a = t[0]
		b = t[1]
		c = t[2]
		print a,b,c
							
		
		
		
		
		
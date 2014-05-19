# coding:utf-8

import sys
import re

# 「仙台市・・・区」を含む表現を抽出する（区は３文字以内とする）
p = re.compile(u'仙台市.{1,3}区')

for a in sys.stdin.readlines():
	q = unicode(a, 'utf-8')
	searched = p.search(q)
	if searched:
		print searched.group()
	
		
		
		
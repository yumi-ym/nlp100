# coding:utf-8

import sys
import re
p = re.compile(r'拡散希望')

for a in sys.stdin.readlines():
	searched = p.search(a)
	if searched:
		print a


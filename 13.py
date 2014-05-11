# coding:utf-8

import sys
import re
p = re.compile(r'\S+RT')
for a in sys.stdin.readlines():
	matched = p.match(a)
	if matched:
		q = a.split('RT')	
		print q[0]
		



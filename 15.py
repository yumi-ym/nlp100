# coding:utf-8
		
import sys
import re

for a in sys.stdin.readlines():
	print re.sub(r'@(.+?)\b',r'<a href="https://twitter.com/#!/\1">@\1</a>',a)
		
	


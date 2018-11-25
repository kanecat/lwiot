#!usr/bin/env python3
# -*- coding utf-8 -*-

'a test module'

__author__='Kane lu'
import sys
def test():
	args=sys.argv
	if len(args)==1:
		print('hello,python!')
	elif len(args)==2:
		print('Hello,%s!' % args)
	else:
		print('Too many argument!')
if __name__ == '__main__':
	test()

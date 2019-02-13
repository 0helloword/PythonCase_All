#-*- coding: utf-8 -*-
#判断两个list值是否相同

import os,sys



def dif(a,b): 
	#c=list(set(a) ^ set(b))
	#找出a里面存在的，b里面不存在的
	c=list(set(a).difference(set(b)))
	return c
pass

if __name__ == "__main__":
	 pass
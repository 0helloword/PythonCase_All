#!/usr/bin/python
# -*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def stringToList(string):
    tolist = string.replace(' ','').split(',')
    return tolist
# -*- coding: utf-8 -*-
import os
import random


def get_wechat_code():
    chars = 'abcdefghijklmnopqrstuvwxyz123456789'
    wechat_code_str = ''
    for i in range(0, 11):
        wechat_code_str += chars[random.randint(1, len(chars)-1)]
        pass
    return wechat_code_str
pass

if __name__ == '__main__':
    print(get_wechat_code())

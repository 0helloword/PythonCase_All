# -*- coding: utf-8 -*-
import os
import random


def get_qq_code():
    chars = '123456789'
    qq_code_str = ''
    for i in range(0, 10):
        qq_code_str += chars[random.randint(1, len(chars)-1)]
        pass
    return qq_code_str
pass

if __name__ == '__main__':
    print(get_qq_code())

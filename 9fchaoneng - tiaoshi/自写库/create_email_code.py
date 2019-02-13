# -*- coding: utf-8 -*-
import os
import random


def get_email_code():
    chars = 'abcdefghijklmnopqrstuvwxyz123456789'
    email_code_str = ''
    for i in range(0, 10):
        email_code_str += chars[random.randint(0, len(chars)-1)]
        pass
    email_code_str += '@163.com'
    return email_code_str
pass

if __name__ == '__main__':
    print(get_email_code())
    pass

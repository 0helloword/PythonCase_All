# -*- coding: utf-8 -*-
import os
import random

phone_number_list = [133, 153, 180, 181, 189, 130, 131, 132, 145, 155, 156, 185, 186, 134, 135, 136, 137,
                                 138, 139, 147, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188]


def get_phone_number():
    phone_number = ''
    eight_number_count = 0
    phone_three_start_number = phone_number_list[random.randint(0, len(phone_number_list)-1)]
    phone_number += str(phone_three_start_number)
    while eight_number_count < 8:
        phone_number += str(random.randint(0, 9))
        eight_number_count += 1
        pass
    return phone_number
pass

if __name__ == '__main__':
    print(get_phone_number())
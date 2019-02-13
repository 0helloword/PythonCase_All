# -*- coding: utf-8 -*-

import os
import random

check_code_str = '10X98765432'
widget_code_list = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
file_address = 'G:\\pythonCase\\idCards.txt  '
file_address_read = file_address.replace('\\', '/')
file = open(file_address_read, 'r')

area_code_list = []
for line in file.readlines():
    area_code_list.append(line.strip('\n'))
file.close()


def to_date_str(date_int):
    if date_int < 10:
        date_str = '0' + str(date_int)
        pass
    else:
        date_str = str(date_int)
        pass
    return date_str


def get_id_card():
    id_card_str = ''
    id_card_str += area_code_list[random.randint(0, len(area_code_list) - 1)]
    id_card_str += str(random.randint(1963, 1997))
    id_card_str += to_date_str(random.randint(1, 12))
    id_card_str += to_date_str(random.randint(1, 28))
    id_card_str += str(random.randint(0, 9))
    id_card_str += str(random.randint(0, 9))
    id_card_str += str(random.randint(0, 9))
    sum_17 = 0
    for i in range(0, 17):
        sum_17 += int(id_card_str[i]) * int(widget_code_list[i])
        pass
    last_code_int = check_code_str[sum_17 % 11]
    id_card_str += str(last_code_int)
    return id_card_str
    pass
pass

if __name__ == '__main__':
    print(get_id_card())






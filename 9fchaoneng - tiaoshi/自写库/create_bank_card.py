# -*- coding: utf-8 -*-

import random
import math


def efficient_bank_no(bank_no_list):
    sum_0 = 0
    sum_1 = 0
    bank_no_list.reverse()
    for i in range(0, len(bank_no_list)):
        if i % 2 == 0:
            sum_0 += int(bank_no_list[i])
            pass
        else:
            if int(bank_no_list[i]) * 2 >= 10:
                sum_1 += (int(bank_no_list[i]) * 2 - 9)
                pass
            else:
                sum_1 += (int(bank_no_list[i]) * 2)
                pass
            pass
        pass
    bank_no_list.reverse()
    bank_no_list[15] = int(math.ceil((sum_1 + sum_0) * 1.0 / 10) * 10 - (sum_0 + sum_1))
    pass
pass


def get_bank_no():
    bank_number_str = ''
    bank_number_list = [6, 2, 2, 5, 8, 8, 7, 8]
    for a in range(8, 15):
        bank_number_list.append(random.randint(0, 9))
        pass
    bank_number_list.append(0)
    efficient_bank_no(bank_number_list)
    for each_number in bank_number_list:
        bank_number_str += str(each_number)
        pass
    return bank_number_str
    pass
pass


if __name__ == '__main__':
    print(get_bank_no())
    pass

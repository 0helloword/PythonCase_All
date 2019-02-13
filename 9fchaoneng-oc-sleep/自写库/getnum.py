# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import Select
from _ast import Num


def get_table_num():
	sleep(2)
    nextpage=driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[3]/div/div/div[2]/a[1]").text
    
    if nextpage=='下一页':
        driver.find_element_by_link_text('最后一页')
        pass
    else:
        print '仅有一页'
        pass
    pass
    sleep(2)
    pages=driver.find_element_by_id("pageInput").get_attribute("value")
    trnum=driver.find_elements_by_tag_name("tr")
    num=pages*20+(trnum-1)
    return num
pass
         
driver = webdriver.Chrome() 

if __name__ == '__main__':
    pass
    
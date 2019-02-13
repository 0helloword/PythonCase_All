from selenium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
class test1(unittest.TestCase):
    
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.baseurl="http://123.57.78.243:7778/initLogin"
		self.driver.maximize_window()
        
        
        
        
    def dengLu(self):
        browser=self.driver
        
        browser.get(self.baseurl)
		
		browser.find_element_by_id("username").send_keys("999111")
        browser.find_element_by_id("password").send_keys("cyj111")
        browser.find_element_by_id("loginButton").click()
		
        

        #调用isElementExist方法，判断元素是否存在
        flag=test1.isElementExist(self, "//*[@id="title:1512794587225"]")         
        
		 if flag:
            
            print("有弹窗")
            
            
        else:
            print("没有弹框")

        
        
        
#   该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false        
    def isElementExist(self,element):
        flag=True
        browser=self.driver
        try:
            browser.find_element_by_xpath(element)
            return flag
        
        except:
            flag=False
            return flag
def isElementExist(self,element):
    flag=True
    browser=self.driver
    try:
        browser.find_element_by_class_name(element)
        browser.close()  
        return flag
    except:
        flag=False
        browser.close()  
        return flag
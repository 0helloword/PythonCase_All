#-*-coding:utf-8-*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import requests,xlrd

def posttest2(url,data,headers):
    #workbook=xlrd.open_workbook(filepath)
    #sheet=workbook.sheet_by_index(0)
	#sheet=workbook.sheet_by_name(u'个人信息')
    #nrows=sheet.nrows
    #if nrows==2:
        #url = str(sheet.cell(0, 0).value)
        #headers = eval(str(sheet.cell(1, 0).value))
        #req=requests.post(url=url,data=None,headers=headers)
    #else:
        #url = str(sheet.cell(0, 0).value)
    #headers = eval(str(sheet.cell(1, 0).value))
    #body ={"productId":"384"}
    req = requests.post(url=url, data=data, headers=headers)
    return req.text,req.status_code,req.json()['status']
pass

if __name__ == "__main__":
	pass
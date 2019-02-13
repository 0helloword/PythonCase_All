import unittest
from test_case.注册模块 import zhuce
from test_case.登录模块 import denglu
from test_case.完善资料模块 import ziliao
from test_case.消费账单模块 import repayment
from test_case.会员服务模块 import consumption
from test_case.额度分期 import withdraw
def return_suite():
    #创建一个测试套件对象
    suite = unittest.TestSuite()
    #创建一个加载器对象
    loader = unittest.TestLoader()
    #将测试用例加载到测试套件中
    # suite.addTests(loader.loadTestsFromTestCase(zhuce.Register))#注册
    # suite.addTests(loader.loadTestsFromTestCase(denglu.Login))#登录
    # suite.addTests(loader.loadTestsFromTestCase(ziliao.Information))#完善资料--退出登录
    # suite.addTests(loader.loadTestsFromTestCase(repayment.repayment))#消费账单--登录完成
    # suite.addTests(loader.loadTestsFromTestCase(consumption.consumption))#会员服务
    # suite.addTests(loader.loadTestsFromTestCase(withdraw.withdraw))#额度分期
    return suite




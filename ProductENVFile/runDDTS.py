import unittest
import time
from ToolsFile import HTMLTestReportEN
from ProductENVFile import TestCasesLib


# class BVTs(unittest.TestCase):
    # TODO: 验证多个Page 都分别引用GUIElements对象是，该对象在内存中创建几次，在GUIElement的类变量声明段中打印时间，或输出。
class BVTTest(unittest.TestCase):
    # def callUserRegister_1001(self):
    #     return True
    # def callUserLogin_1002(self):
    #     TestCasesLib.testCasesLib.tc_UserLogin_1002()
    # def callUserDeposit_1003(self):
    #     TestCasesLib.testCasesLib.tc_UserDeposit_1003()
    def calltc_addFund(self):
        TestCasesLib.adminUserTCs.tc_addFund()

def Suite():
    '''
    () -> suite object
    Return the suite object which stored the test cases suite declared in test classes.
    '''
    suite = unittest.TestSuite()
    # suite.addTest(BVTTest('callUserRegister_1001'))
    # suite.addTest(BVTTest('callUserLogin_1002'))
    suite.addTest(BVTTest('calltc_addFund'))
    return suite
if __name__ == '__main__':
    filename = 'AgmBrokerTestResult.html'
    #定义报告文件权限，wb，表示有读写权限
    fp = open(filename,'wb')
    runner = HTMLTestReportEN.HTMLTestRunner(
        stream=fp,
        title='The testing report for https://www.agmbroker.com/',
        description='This is our auto web testing result summary.')
    # 执行测试
    runner.run(Suite())

    # 关闭文件，否则会无法生成文件
    time.sleep(2)
    fp.close()
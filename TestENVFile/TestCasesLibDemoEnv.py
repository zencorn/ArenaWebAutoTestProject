from PageComponents.HtmlPageElements import *
import time
from ToolsFile.Utility import *

class testCasesLib():
    def tc_UserRegist_1001():
        pageAgmHome.linkLogin().click()
        time.sleep(2)
        pageRegist.txtUserName().click()

    def tc_UserDeposit_1003():
        sysConf = TestUtility.conf
        str_UserName = sysConf['TestEndUserInfo']['userName']
        str_UserPWD = sysConf['TestEndUserInfo']['userPWD']
        pageUserLogin.iconEnglish().click()
        time.sleep(1)
        pageUserLogin.txtLoginUser().click()
        pageUserLogin.txtLoginUser().send_keys(str_UserName)
        pageUserLogin.txtUserPWD().click()
        pageUserLogin.txtUserPWD().send_keys(str_UserPWD)
        pageUserLogin.txtVerifyCode().click()
        # TODO: Verify Code
        time.sleep(5)
        pageUserLogin.btnLogin().click()
        time.sleep(4)
        pageUserInfo.btnFunMenu().click()
        pageUserInfo.linkDeposit().click()

    def tc_UserLogin_1002():
        sysConf = TestUtility.conf
        str_UserName = sysConf['ProductEndUserInfo']['userName']
        str_UserPWD = sysConf['ProductEndUserInfo']['userPWD']
        # pageAgmHome.linkLogin().click()
        pageUserLogin.txtLoginUser().click()
        pageUserLogin.txtLoginUser().send_keys(str_UserName)
        pageUserLogin.txtUserPWD().click()
        pageUserLogin.txtUserPWD().send_keys(str_UserPWD)
        pageUserLogin.txtVerifyCode().click()
        # TODO: Verify Code
        time.sleep(5)
        pageUserLogin.btnLogin().click()
class adminUserTCs():
    def tc_addFund():
        pageAdmin.inconEnglish().click()
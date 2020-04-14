from PageComponents.HtmlPageElements import *


from ToolsFile.Utility import *

class testCasesLib():

    def tc_UserRegist_1001():
        pageAgmHome.linkLogin().click()
        time.sleep(2)
        pageRegist.txtUserName().click()

    def tc_UserDeposit_1003():
        sysConf = TestUtility.conf
        str_UserName = sysConf['EndUserInfo']['userName']
        str_UserPWD = sysConf['EndUserInfo']['userPWD']
        pageAgmHome.linkLogin().click()
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
        str_UserName = sysConf['EndUserInfo']['userName']
        str_UserPWD = sysConf['EndUserInfo']['userPWD']
        pageAgmHome.linkLogin().click()
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
        pageAdmin.changeAdminPortal()
        pageAdmin.inconEnglish().click()
        TestUtility.sleepTime(8)
        sysConf = TestUtility.conf
        str_AdminName = sysConf['AdminInfo']['AdminName']
        str_AdminPWD = sysConf['AdminInfo']['AdminPWD']
        pageAdmin.txtAdmin().click()
        pageAdmin.txtAdmin().send_keys(str_AdminName)
        TestUtility.sleepTime(1)
        pageAdmin.txtPwdAdmin().send_keys(str_AdminPWD)
        TestUtility.sleepTime(1)
        pageAdmin.txtVerifyCode().click()
        time.sleep(5)
        pageAdmin.btnLogin().click()
        pageAdmin.btnSelLanguage().click()
        pageAdmin.btnEnglish().click()

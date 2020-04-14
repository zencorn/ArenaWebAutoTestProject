__author__ = 'admin'


from ToolsFile import Utility
from selenium import webdriver
import time

strUserLoginPageURL = 'NULL'
class webTestDriver():
    print('==== webTestDriver ====== ')
    option = webdriver.ChromeOptions();
    option.add_experimental_option("excludeSwitches", ['enable-automation']); # To set the infobar of chrome disappear.
    chrBrowser = webdriver.Chrome(options = option)  # We are using the Chrom as our test execution browser.
    strUserLoginPageURL = 'https://usercenter.agmbroker.com/Login' # The target of testing site
    chrBrowser.get(strUserLoginPageURL)
    time.sleep(2)
    chrBrowser.maximize_window()
    def __init__(self,strName):
        print('==== init ====== ')
        self.name = strName

#TODO: 尝试将不同测试页面封装在GUIElements这个包中，然后定各页面类。 将webTestDriver 中的类成员变量放入初始化中，定一个可被其它页面类引用直接调用的工具对象
    def txtBaiduSearch(self):
        txtBaiduSearch = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="kw"]')
        return txtBaiduSearch
    def btnBaiduSearch(self):
        btnBaiduSearch = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="su"]')
        return btnBaiduSearch
    def linkResOne(self,browser):

        linkResOne = browser.find_element_by_xpath('//*[@id="1"]')

        #linkResOne = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="1"]/*[contains(local-name(),"data-click")]')

        print(linkResOne.tag_name)


        return linkResOne


    def closeBrowser(self):
        MTGUI().b.close()
        return
# =========== Temp Using ========================
    def openNewTempPage():
        str_TemplPageURL = 'https://www.nypl.org/events/calendar'
        webTestDriver.chrBrowser.get(str_TemplPageURL)
    def cateGroup():
        grpURL = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="calendar-filter"]/form/div/div[4]/h5')
        return grpURL
# =========== Login Page & page elements ==========
    def switchUserLoginPage():
        str_switchUserLoginPage = 'https://ctp.360jincai.com/app/login.html'
        webTestDriver.chrBrowser.get(str_switchUserLoginPage)
# =========== Admin Login Page & page elements ==========
    def switchAdminPage():
        # str_AdminLoginPageURL = 'http://54.223.229.9:5202/CTPAdmin/app/login.html'
        str_AdminLoginPageURL = 'https://ctp.360jincai.com/CTPAdmin/app/login.html'


        webTestDriver.chrBrowser.get(str_AdminLoginPageURL)
    def txtAdminUserName():
        txtAdminUserName = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="username"]')
        return txtAdminUserName
    def txtAdminPwd():
        txtAdminUserName = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="password"]')
        return txtAdminUserName
# =========== 网站首页 及 登录 页面元素 ==========
    def linkLogin():
        # linkLogin = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div/ul/li/a[4]')
        linkLogin = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="loginStatus"]')
        return linkLogin

    def linkRegister():
        linkRegister = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="li_3"]/a')

        # /html/body/div[1]/div/div[2]/ul/li[6]/a
        # //*[@id="nav"]/ul/li/a[5]
        # //*[@id="LoginForm"]/div[4]/div/a
        return linkRegister

    def txtUserName():
        txtUserName = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="username"]')
        return txtUserName

    def txtPWD():
        txtPWD = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="password"]')
        return txtPWD

    def btnLogin():
        btnLogin = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[2]/form/div[4]/button')
        return btnLogin

# =========== 用户个人管理中心 ==========
    def linkSysManage():
        linkSysManage = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[5]/a/span[1]')

        # //*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a
        return linkSysManage
    def linkUserManage():
        linkUserManage =  webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[4]/div[1]/div/ul/li[5]/ul/li[3]/a')
        return linkUserManage
    def optionRowOne():
        optionRowOne = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/label/span')
        return  optionRowOne
    def btnDelUserRow():
        btnDelUserRow = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="btn_delete"]')
        return btnDelUserRow
    def btnConfirmDelDialog():
        btnConfirmDelDialog = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[6]/div[7]/div/button')
        return btnConfirmDelDialog
    def btnNotifyDialog():
        btnNotifyDialog = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[6]/div[7]/div/button')
        return btnNotifyDialog

# =========== 用户注册页页面元素 ==========

    def btnSendVerifyCode():
        btnSendVerifyCode = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="messageCode"]')
        return btnSendVerifyCode
    def txtPhoneNum():
        txtPhoneNum = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="phone"]')
        # //*[@id="RegisterForm"]/div[1]/div/div/div/input
        return txtPhoneNum
    def txtVerifyCode():
        txtVerifyCode = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="verification"]')
        # //*[@id="RegisterForm"]/div[2]/div[1]/div/div/input
        return txtVerifyCode
    def txtRegPWD():
        txtRegPWD = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="password"]')
        # //*[@id="RegisterForm"]/div[3]/div/div/div/input
        return txtRegPWD
    def txtRegSecondPWD():

        # txtRegSecondPWD = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[2]/form/div[5]/div/input')
        txtRegSecondPWD = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="qpassword"]')


        # print(txtRegSecondPWD.tag_name)
        # print(txtRegSecondPWD.text)
        return txtRegSecondPWD
    def optionLink():
        optionLink = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="register-form"]/div[6]/div/div/ins')
        return optionLink
    def btnRegis():
        btnRegis = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="register-form"]/div[7]/button')
        return btnRegis
    def btnRegistSuccess():
        # btnRegistSuccess = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[4]/div[7]/div/button')
        btnRegistSuccess = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div[5]/div[7]/div/button')

        return btnRegistSuccess
# ========
    def lblMTAccout(self):
        lblMTAccout = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a/span')
        return lblMTAccout

    def lblCurrentUser(self):
        lblCurrentUser = webTestDriver.chrBrowser.find_element_by_id('HeaderCurrentUserName')
        # lblCurrentUser = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="HeaderCurrentUserName"]')
        return lblCurrentUser

    def lblRegisterSuccess(self):
        lblRegisterSuccess = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/div/div[2]/div/h4')
        return lblRegisterSuccess
# ===================================== MT Link CTP Operation Actions =========================
    def linkMTAccount(self):

        linkMTAccount = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a')
        return linkMTAccount

    def btnAddMTAccount(self):

        btnAddMTAccount = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[3]/a/span')
        return btnAddMTAccount

    def btnAction(self):
        btnAction = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[9]/a')
        return btnAction

    def btnLink(self):
        btnLink = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[9]/ul/li[1]/a')
        return btnLink

    def btnSaveCTPLink(self):
        btnSaveCTPLink = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="MtAccountEditModal"]/div/div/div[3]/button[2]')
        return btnSaveCTPLink

    def lblCTPAccountLink(self):
        lblCTPAccountLink = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[5]')
        return lblCTPAccountLink
# ===================================== CTP Operation Actions =================================
    def linkCTPAccount(self):
        linkCTPAccount = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[4]/a')
        #linkCTPAccount = myTestUtility.get_ele_times(webTestDriver.chrBrowser,50,lambda d:webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="leftsidebar"]/div[2]/div/ul/li[4]/a'))
        return linkCTPAccount

    def btnAddCTP(self):
        btnAddCTP = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/button')

        return  btnAddCTP

    def txtInvsID(self):
        txtInvsID = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[1]/div[1]/div/div/input')
        return txtInvsID
    def txtInvsPWD(self):
        txtInvsPWD = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[1]/div[2]/div/div/input')
        return txtInvsPWD
    def txtFee(self):
        txtFee = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="create-ctpaccount-details"]/div[2]/div/div/div/input')
        return txtFee
    def btnSaveCTP(self):
        btnSaveCTP = webTestDriver.chrBrowser.find_element_by_xpath('//*[@id="CtpAccountCreateModal"]/div/div/div[2]/form/div[2]/button[2]')
        return btnSaveCTP
    def lblCTPAccount(self):
        lblCTPAccount = webTestDriver.chrBrowser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div/div[2]/table/tbody/tr/td[2]')
        return lblCTPAccount
    def openTempPage(self):
        '''
        Open one Temp page for debugging
        '''
        str_TempPageUrl = 'https://www.baidu.com'
        webTestDriver.chrBrowser.get(str_TempPageUrl)



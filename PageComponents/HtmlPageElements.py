__author__ = 'admin'

from ToolsFile.Utility import *
from selenium import webdriver
import time



class webDrive():
    def __init__(self,siteStr):
        # option = webdriver.ChromeOptions();
        # option = webdriver.FirefoxOptions
        # option.add_experimental_option("excludeSwitches", ['enable-automation']); # To set the infobar of chrome disappear.
        self.chrBrowser = webdriver.Chrome()  # We are using the Chrom as our test execution browser.
        # self.chrBrowser = webdriver.Firefox(options=option)
        # strUserLoginPageURL = 'https://www.agmbroker.com/' # The target of testing site
        # self.strUserLoginPageURL = 'https://usercenter.agmbroker.com/Login'  # The target of testing site
        self.strUserLoginPageURL = siteStr
        self.chrBrowser.get(self.strUserLoginPageURL)
        time.sleep(2)
        self.chrBrowser.maximize_window()

confobj = TestUtility.conf
webDriveObj = webDrive(confobj['ProductURL']['AgmBrokerHome'])
# webDriveObjCRM = webDrive('https://usercenter.agmbroker.com')


class pageAdmin():
    def changeAdminPortal():
        webDriveObj.chrBrowser.get(confobj['ProductURL']['AgmAdmin'])

    def inconEnglish():
        inconEnglish = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="ChangeUS"]')
        return inconEnglish
    def txtAdmin():
        txtAdmin = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="AdminLoginUsername"]')
        return txtAdmin
    def txtPwdAdmin():
        txtPwdAdmin = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="AdminLoginPassword"]')
        return txtPwdAdmin
    def txtVerifyCode():
        txtVerifyCode = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="AdminLoginCaptcha"]')
        return txtVerifyCode
    def btnLogin():
        btnLogin = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="AdminLoginButton"]')
        return btnLogin
class PageAmgmHome():
    def linkLogin():
        linkLogin = 1
        return  linkLogin
class pageAgmHome():
    def linkCanlender():
        linkCanlender = webDriveObj.chrBrowser.find_element_by_xpath('/html/body/div[2]/div/ul/li[3]/a/span')
        return linkCanlender
    def linkOpenAcc():
        linkOpenAcc = webDriveObj.chrBrowser.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/div/div/div/div/a[1]')
        return linkOpenAcc
    def linkLogin():
        linkLogin = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="text-11"]/div/div/a[2]')
        return linkLogin
class pageUserInfo():
    def btnFunMenu():
        btnFunMenu = webDriveObj.chrBrowser.find_element_by_link_text('Fund Mgt')
        # btnFunMenu = webDriveObj.chrBrowser.find_element_by_xpath('/html/body/div[1]/div/div/div/ul/li[3]/a/span/text()')
        # '/html/body/div[1]/div/div/div/ul/li[3]/a/span/text()'
        ''
        return btnFunMenu
    def linkDeposit():
        linkDeposit = webDriveObj.chrBrowser.find_element_by_xpath('/html/body/div[1]/div/div/div/ul/li[3]/ul/li[1]/a')
        return linkDeposit
class pageUserLogin():
    def txtVerifyCode():
        txtVerifyCode = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="LoginCaptcha"]')
        return txtVerifyCode
    def btnLogin():
        btnLogin = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="user-login"]')
        return btnLogin
    def txtUserPWD():
        txtUserPWD = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="password"]')
        return txtUserPWD
    def iconEnglish():
        iconEnglish = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="ChangeUS"]/a/img')
        return iconEnglish
    def txtLoginUser():
        # webDriveObj.chrBrowser.switch_to.window(webDriveObj.chrBrowser.window_handles[1])
        time.sleep(2)
        txtLoginUser = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="username"]')

        return txtLoginUser
class pageRegist():
    def txtOpenEmail():
        txtOpenEmail = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="Email"]')
        return txtOpenEmail
    def txtOpenUserName():
        webDriveObj.chrBrowser.switch_to.window(webDriveObj.chrBrowser.window_handles[1])
        time.sleep(2)
        txtOpenUserName = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="Name"]')
        return txtOpenUserName
    def linkForgetPWD():
        linkForgetPWD = webDriveObj.chrBrowser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/center/div[1]/a')
        return linkForgetPWD
__author__ = 'admin'

import time
import datetime
from selenium import webdriver
from selenium.webdriver.support.select import Select

from ToolsFile.Utility import *




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
# webDriveObj = webDrive(confobj['ProductURL']['ArenaUserPortal'])
# .get('ProductURL').get('arenauserportal')
webDriveObj = webDrive(confobj.get('ProductURL').get('arenauserportal'))
# webDriveObjCRM = webDrive('https://usercenter.agmbroker.com')


class pageAdmin():
    def changeAdminPortal():
        TestUtility.sleepTime(3)
        str_time = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/header/div/div[1]/div/div[1]/span').text
        TestUtility.sleepTime(2)
        str_Time = str_time[13:]
        my_date = datetime.datetime.strptime(str_Time, '%H:%M:%S')

        delta = datetime.timedelta(minutes=5)
        newmins = my_date + delta
        TestUtility.CURRENT_CompeStart_Time = str(newmins)[11:]
        webDriveObj.chrBrowser.get(confobj.get('ProductURL').get('arenaadmin'))
        time.sleep(8)
        # return system_GMT_time
    def btnCompeMaga():
        # TestUtility.sleepTime(3)
        # webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/a[1]/li/span').click()
        time.sleep(2)
        btnCompeMaga = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li[2]').find_element_by_tag_name('div').find_element_by_tag_name('span')
                                                                    # '//*[@id="app"]/div/div[1]/div/ul/div/li[2]/div'
                # btnCompeMaga.click()
        # btnCompeMaga = webDriveObj.chrBrowser.find_elements_by_link_text('比赛管理')
                                                                    # '//*[@id="app"]/div/div[1]/div/ul/div/li[2]/div/span'
        return btnCompeMaga

    def btnChalCompe():
        TestUtility.sleepTime(2)
        btnChalCompe = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/ul/div/li[2]/ul/a[2]/li/span')
        return btnChalCompe
    def btnAddNewChalCompe():
        TestUtility.sleepTime(2)
        btnAddNewChalCompe = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[1]/button[2]/span')
        return btnAddNewChalCompe
    def txtContZhName():
        txtContZhName = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[1]/div/div/input')
        return txtContZhName
    def txtContENName():
        txtContENName = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[2]/div/div/input')
        return txtContENName
    def combTradeTool():
        TestUtility.sleepTime(2)
        combTradeTool = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[3]/div/div/div/input')
        # combTradeTool.click()
        # Select(combTradeTool).select_by_visible_text(text_value)
        return combTradeTool
    def itemTradeTool():
        TestUtility.sleepTime(4)
        combTradeTool = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div[1]/ul/li[1]')
        # '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span'
                                                                     # '/html/body/div[4]/div[1]/div[1]/ul/li[1]/span'
        # print(combTradeTool.tag_name)
        combTradeTool.click()
        return combTradeTool
    def combMT4Group():
        TestUtility.sleepTime(2)
        combMT4Group = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[4]/div/div/div/input')
        return combMT4Group
    def itemMT4Group():
        TestUtility.sleepTime(2)
        itemMT4Group = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[5]/div[1]/div[1]/ul/li[5]').find_element_by_tag_name('span')

            # .find_element_by_tag_name('span')
            # '/html/body/div[5]/div[1]/div[1]/ul/li[1]/span'
        return itemMT4Group
    def txtFreeTimes():
        TestUtility.sleepTime(2)
        txtFreeTimes = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[5]/div/div/input')

        return txtFreeTimes
    def txtTickPrice():
        TestUtility.sleepTime(2)
        txtTickPrice = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[6]/div/div/input')
        return txtTickPrice
    def combContLevl():
        TestUtility.sleepTime(2)
        combContLevl = webDriveObj.chrBrowser.find_element_by_xpath('//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[10]/div/div/div/input')

        return combContLevl
    def itemConLevel(str_level):
        TestUtility.sleepTime(3)
        strLevel = str(str_level)
        TestUtility.sleepTime(2)
        # str_search = '/html/body/div[5]/div[1]/div[1]/ul/li[3]/span'
        # str_search = '/html/body/div[3]/div[1]/div[1]/ul/li[3]'
        # print('New
        # >>>>> '.join(str_search).join(' <<<<'))
        # '/html/body/div[3]/div[1]/div[1]/ul/li[3]/span'
        itemConLevel = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[3]/div[1]/div[1]/ul/li[3]').find_element_by_tag_name('span')
        return itemConLevel
    def txtIniBalance():
        # 帐号初始余额
        txtIniBalance = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[11]/div/div[1]/input')
        return txtIniBalance
    def txtCompeDuration():
        # 比赛时长(天)
        txtCompeDuration = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[12]/div/div/input')
        return txtCompeDuration


    def txtCompStartTime():
        # 比赛时长(天)
        TestUtility.sleepTime(3)
        txtCompStartTime = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div/div[1]/span[2]/div[1]/input')
        return txtCompStartTime
    def btnTimeConfirm():
        '/html/body/div[6]/div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]'
        btnTimeConfirm = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div/div[1]/span[2]/div[2]/div[2]/button[2]')
        return btnTimeConfirm
    def txtCompeStartDate():
        txtCompeStartDate = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[6]/div[1]/div/div[1]/span[1]/div/input')


        return txtCompeStartDate
    def btnCanlendarConfirm():
        btnCanlendarConfirm = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[6]/div[2]/button[2]/span')
        return btnCanlendarConfirm

    def txtRegistEndCalendar():
        txtRegistEndCalendar = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[2]/form/div[14]/div/div/input')
        return txtRegistEndCalendar
    def txtRegistEndDate():
        TestUtility.sleepTime(2)
        txtRegistEndDate = webDriveObj.chrBrowser.find_element_by_xpath(
            '/html/body/div[7]/div[1]/div/div[1]/span[1]/div/input')
        return txtRegistEndDate
    def btnRegistEndConfirm():
        TestUtility.sleepTime(2)
        btnRegistEndConfirm = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]/span')
        return btnRegistEndConfirm
    def confPanel():
        TestUtility.sleepTime(2)
        confPanel = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[7]/div/div[2]')
        # '//*[@id="app"]/div/div[2]/section/div/div[7]/div/div[2]/form/button/i'
        # print(confPanel.tag_name)
        return confPanel
    def btnNextStep():
        TestUtility.sleepTime(2)
        btnNextStep = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[4]/div/div[3]/div/button[2]/span')
        return btnNextStep
    def btnAddLevel():
        btnAddLevel = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[7]/div/div[2]/form/button/i')
        return btnAddLevel
    def txtLveOneReward():
        TestUtility.sleepTime(2)
        txtLveOneReward = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[7]/div/div[2]/div/div[3]/table/tbody/tr/td[2]/div/div/input')
        return txtLveOneReward
    def txtLevOneFaileLine():
        TestUtility.sleepTime(2)
        txtLevOneFaileLine = webDriveObj.chrBrowser.find_element_by_xpath(
            '//*[@id="app"]/div/div[2]/section/div/div[7]/div/div[2]/div/div[3]/table/tbody/tr/td[3]/div/div/input')
        return txtLevOneFaileLine

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
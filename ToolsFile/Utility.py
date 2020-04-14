__author__ = 'admin'
import datetime
import time
import xlrd
import xlsxwriter
import openpyxl
import random
import requests
import configparser
import os
# import jenkins




class TestUtility:
    conf = configparser.ConfigParser()
    strSysConfig = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'SystemConfig.ini'
    conf.read(strSysConfig, encoding="utf-8")
    runType = int(conf['ExecEnvType']['execType'])
    strConfigFile=1
    if(runType == 1):
        strConfigFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'ProConfigure.ini'
    elif(runType == 0):
        strConfigFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'DemoENVProConfigure.ini'

    conf.read(strConfigFile, encoding="utf-8")
    strFileName = r'd:\\TestResultLog_'+ str(datetime.date.today().strftime("%Y_%m_%d")) + '.txt'
    # def __init__(self):
        #filePath = cf['LogFile']['userPWD']

    def sleepTime(intSeconds):
        time.sleep(intSeconds)
    def convFlStr(self,val):
        if isinstance(val,float):
            val = str(int(val))
        return val

    def getExcelFile(path):
        try:
            xls = xlrd.open_workbook(path)
            # print(len(xls.sheets()))
            value_rows = []
            sheetOne = xls.sheets()[0]
            rows = sheetOne.nrows
            for r in range(1,rows):
                strVal =sheetOne.row_values(r)
                value_rows.append(strVal)
        except:
            print(path)
        return value_rows

    def creaLogFile(self):
        if(os.path.exists(self.strFileName)):
            return
        else:
            f = open(self.strFileName,'w')
            f.close()
        return

    def resLog(strTCName,strRes):
        timeStamp = str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        try:
            strIni = 'TestResLog : ' + strTCName
            resLog = strIni + '_' + strRes
            finaStr = resLog + '__' + timeStamp + '\n'
            fp = open(TestUtility.strFileName,'a',encoding='utf-8')
            fp.write(finaStr)
            fp.close()
        except:
            print('System Exception Error!')
        return

    def infoLog(strMsg):
        timeStamp = str(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        try:
            strIni = '---------> '
            msgLog = 'TestMsgLog:__' + strMsg
            finaStr = strIni + msgLog + '__' + timeStamp + '\n'
            fp = open(TestUtility.strFileName,'a',encoding='utf-8')
            fp.write(finaStr)
            fp.close()
        except:
            print('System Exception Error!')
        return

    def getFile(path):
        file = open(path)
        for line in file:
            print(line.strip())
        return

    def getPhoneNum(*args):
        prelist=["130","131","132","133","134","135","136","137","138","139","147","150","151","152","153","155","156","157","158","159","186","187","188"]
        return random.choice(prelist)+"".join(random.choice("0123456789") for i in range(8))
    def getVerifyCode(self,strPhoneNumber):
        registUrl = 'http://13.124.220.217:8010/Account/GetCheckCode?phoneNum=' + strPhoneNumber
        regisCode = requests.get(registUrl)
        return regisCode.text

    # def get_ele_times(self,driver,times,func):

        # return WebDriverWait(driver,times).until(func)

    def get_Jenkins():
        JenkinsServer = jenkins.Jenkins('http://localhost:8080',username='admin',password = 'Admin')
        print('Here')
        user = JenkinsServer.get_whoami()
        print(user['fullName'])
        version = JenkinsServer.get_version()
        print('Hello %s from Jenkins %s' % (user,version))
        return












'''
    def CommonUserLogin(self,):
        MTWeb.txtUserName().click()
        MTWeb.txtUserName().send_keys(cf['UserInfo']['userName'])
        MTWeb.txtPWD().click()
        MTWeb.txtPWD().send_keys(cf['UserInfo']['userPWD'])
        MTWeb.btnLogin().click()
        sleep(3)
'''


__author__ = 'admin'
import datetime
import time
import xlrd
import os
import xlsxwriter
import openpyxl
import random
import requests
import configparser
import os

import win32clipboard

current_dir = os.path.abspath(__file__)

# import jenkins

class SelfDictionary(dict):
    """ custom dict."""
    # TODO: https://www.jianshu.com/p/61c10a59fdab
    def __getattr__(self, key):
        return self.get(key, None)

    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

class ConfigTool:
    def __init__(self,filename,cfg=None):
        """ @param file_name: file name without extension.
            @param cfg: configuration file path.

        """
        env = {}
        for key , value in os.environ.items():
            if key.startswith('TEST_'):
                env[key] = value
        config = configparser.ConfigParser(env)
        if cfg:
            config.read(cfg)
        else:
            config.read(os.path.join(os.path.dirname(current_dir),
                                     filename),encoding='utf-8')
        for section in config.sections():
            setattr(self,section,SelfDictionary())
            for name,raw_value in config.items(section):
                try:
                    # Ugly fix to avoid '0' and '1' to be parsed as a
                    # boolean value.
                    # We raise an exception to goto fail^w parse it
                    # as integer.
                    if config.get(section, name) in ["0", "1"]:
                        raise ValueError
                    value = config.getboolean(section, name)
                except ValueError:
                    try:
                        value = config.getint(section, name)
                    except ValueError:
                        value = config.get(section, name)
                setattr(getattr(self,section),name,value)
    def get(self,section):
        """Get option.
            @param section: section to fetch.
            @return: option value.
        """
        try:
            return getattr(self,section)
        except AttributeError as e:
            return False


conf = ConfigTool('SystemConfig.ini')

class TestUtility:
    CURRENT_SYSTEM_DATE = 'May 01, 2020'
    CURRENT_SYSTEM_TIME = '02:36:13'
    CURRENT_CompeStart_Time = '11:22:00'
    CURRENT_CompeStart_Date = '2020-05-02'
    CURRENT_RegisEndDate = '1900-01-01'


    runType = int(conf.get('ExecEnvType').get('exectype'))

    strConfigFile=1
    if(runType == 1):
        strConfigFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'ProConfigure.ini'
    elif(runType != 1):
        strConfigFile = os.path.dirname(os.path.abspath(__file__)) + "\\" + 'DemoENVProConfigure.ini'

    # conf.read(strConfigFile, encoding="utf-8")
    conf = ConfigTool(strConfigFile)
    strFileName = r'd:\\TestResultLog_'+ str(datetime.date.today().strftime("%Y_%m_%d")) + '.txt'
    # def __init__(self):
        #filePath = cf['LogFile']['userPWD']


    def getRegisEndTime(dateStart):
        str_year = str(dateStart[0:4]) + '-'
        str_month = str(dateStart[4:6])+ '-'
        str_day = dateStart[6:]
        str_fulldate = str_year + str_month + str_day
        my_date = datetime.datetime.strptime(str_fulldate, '%Y-%m-%d')
        conf = ConfigTool(TestUtility.strConfigFile)
        str_dur = conf.get('ArenaChallengeCompetitionInfo').get('competition_duration')
        int_duran = int(str_dur)
        delta = datetime.timedelta(days=int_duran)
        newdate = my_date + delta
        return str(newdate)
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

    # def get_Jenkins():
    #     JenkinsServer = jenkins.Jenkins('http://localhost:8080',username='admin',password = 'Admin')
    #     print('Here')
    #     user = JenkinsServer.get_whoami()
    #     print(user['fullName'])
    #     version = JenkinsServer.get_version()
    #     print('Hello %s from Jenkins %s' % (user,version))
    #     return












'''
    def CommonUserLogin(self,):
        MTWeb.txtUserName().click()
        MTWeb.txtUserName().send_keys(cf['UserInfo']['userName'])
        MTWeb.txtPWD().click()
        MTWeb.txtPWD().send_keys(cf['UserInfo']['userPWD'])
        MTWeb.btnLogin().click()
        sleep(3)
'''


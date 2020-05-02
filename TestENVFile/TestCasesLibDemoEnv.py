from PageComponents.HtmlPageElements import *
from ToolsFile.Utility import *
from selenium.webdriver.common.keys import Keys

sysConf = TestUtility.conf

class testCasesLib():
    def tc_UserRegist_1001():
        pageAgmHome.linkLogin().click()
        time.sleep(2)
        pageRegist.txtUserName().click()

    def tc_UserDeposit_1003():
        sysConf = TestUtility.conf
        # webDrive(confobj.get('ProductURL').get('arenauserportal'))
        # str_UserName = sysConf['TestEndUserInfo']['userName']
        # str_UserPWD = sysConf['TestEndUserInfo']['userPWD']
        str_UserName = sysConf.get('TestEndUserInfo').get('userName')
        str_UserPWD = sysConf.get('TestEndUserInfo').get('userpwd')
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

        str_UserName = sysConf['ProductEndUserInfo']['userName']
        str_UserPWD = sysConf['ProductEndUserInfo']['userPWD']
        # pageAgmHome.linkLogin().click()
        pageUserLogin.txtLoginUser().click()
        pageUserLogin.txtLoginUser().send_keys(str_UserName)
        pageUserLogin.txtUserPWD().click()
        pageUserLogin.txtUserPWD().send_keys(str_UserPWD)
        pageUserLogin.txtVerifyCode().click()
        # TODO: Verify Code

        pageUserLogin.btnLogin().click()
class adminUserTCs():
    def tc_AdminAddCompetion():
        pageAdmin.changeAdminPortal()
        pageAdmin.btnCompeMaga().click()
        pageAdmin.btnChalCompe().click()
        pageAdmin.btnAddNewChalCompe().click()

        pageAdmin.txtContZhName().click()
        str_compeName = sysConf.get('ArenaChallengeCompetitionInfo').get(
            'compe_zh_name') + TestUtility.CURRENT_CompeStart_Time
        pageAdmin.txtContZhName().send_keys(str_compeName)

        pageAdmin.txtContENName().click()
        str_compeEnName = sysConf.get('ArenaChallengeCompetitionInfo').get(
            'compe_en_name') + TestUtility.CURRENT_CompeStart_Time
        pageAdmin.txtContENName().send_keys(str_compeEnName)

        pageAdmin.txtFreeTimes().click()
        TestUtility.sleepTime(2)
        strFreeTimes = sysConf.get('ArenaChallengeCompetitionInfo').get('free_times')
        print(strFreeTimes)
        pageAdmin.txtFreeTimes().send_keys(strFreeTimes)

        pageAdmin.combContLevl().click()
        pageAdmin.itemConLevel('Level').click()

        pageAdmin.txtTickPrice().click()
        pageAdmin.txtTickPrice().send_keys(sysConf.get('ArenaChallengeCompetitionInfo').get('ticket_prices'))

        pageAdmin.combTradeTool().click()  # 'Select trading tools'
        pageAdmin.combTradeTool().send_keys('MT4')
        pageAdmin.combTradeTool().send_keys(Keys.ARROW_DOWN)
        pageAdmin.combTradeTool().send_keys(Keys.ENTER)
        pageAdmin.combMT4Group().click()  # 'Open the MT4 group list    '
        TestUtility.sleepTime(2)
        pageAdmin.itemMT4Group().click()  # 'Select the MT4 testing group'

        pageAdmin.txtIniBalance().click()
        pageAdmin.txtIniBalance().send_keys(sysConf.get('ArenaChallengeCompetitionInfo').get('ini_balance'))

        pageAdmin.txtCompeDuration().click()
        pageAdmin.txtCompeDuration().send_keys(sysConf.get('ArenaChallengeCompetitionInfo').get('competition_duration'))

        # 'Making the data calendar get focus'
        pageAdmin.txtCompeDuration().click()
        pageAdmin.txtCompeDuration().send_keys(Keys.TAB)

        # 'Set the mins input value'
        pageAdmin.txtCompStartTime().click()
        pageAdmin.txtCompStartTime().send_keys(Keys.CONTROL, 'a')
        pageAdmin.txtCompStartTime().send_keys(TestUtility.CURRENT_CompeStart_Time)
        TestUtility.sleepTime(2)
        pageAdmin.btnTimeConfirm().click()

        # 'Get the compe start date'
        TestUtility.sleepTime(2)
        pageAdmin.txtCompeStartDate().click()
        pageAdmin.txtCompeStartDate().send_keys(Keys.CONTROL, 'a')
        pageAdmin.txtCompeStartDate().send_keys(Keys.CONTROL, 'c')

        # 'Confirm the canlendar'
        pageAdmin.btnCanlendarConfirm().click()
        # 'Click new step'
        # 'Using the txtCompeDuration as clipboard.'
        TestUtility.sleepTime(2)
        pageAdmin.txtCompeDuration().click()
        pageAdmin.txtCompeDuration().send_keys(Keys.CONTROL, 'a')
        pageAdmin.txtCompeDuration().send_keys(Keys.CONTROL, 'v')
        pageAdmin.txtIniBalance().click()  # 'Switch the focus'
        data = pageAdmin.txtCompeDuration().get_attribute('value')
        TestUtility.sleepTime(2)
        TestUtility.CURRENT_RegisEndDate = TestUtility.getRegisEndTime(data)

        # 'Set regist end date'
        pageAdmin.txtRegistEndCalendar().click()
        pageAdmin.txtRegistEndDate().click()
        pageAdmin.txtRegistEndDate().send_keys(TestUtility.CURRENT_RegisEndDate)
        TestUtility.sleepTime(2)
        pageAdmin.btnRegistEndConfirm().click()

        # 'Restal CompeDuration Value'
        pageAdmin.txtCompeDuration().click()

        pageAdmin.txtCompeDuration().send_keys(Keys.CONTROL, 'a')
        pageAdmin.txtCompeDuration().send_keys(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('competition_duration'))

        pageAdmin.confPanel().click()
        pageAdmin.btnAddLevel().click()
        pageAdmin.txtLveOneReward().click()
        pageAdmin.txtLveOneReward().send_keys(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('reward_points'))
        pageAdmin.txtLevOneFaileLine().click()
        numA = float(str(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('ini_balance')))
        numB = float(str(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('faileline_step')))
        failePoinsts = str(numA - numB)
        pageAdmin.txtLevOneFaileLine().send_keys(failePoinsts)



    def tc_addFund():
        pageAdmin.inconEnglish().click()
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

    def tc_UserJoinChallCompe_1004():
        '''
        () ->
        Simulating the user UI operation of join the ChallenCompe
        '''
        #1: Get the demo user list
        pendingUsers = []
        pendingUsers = TestUtility.getDBMT4UserList()
        # Run the loop
        if(pendingUsers.__len__() > 0):
            for i in range(pendingUsers.__len__()):
                # 2: Login this user
                userName = pendingUsers[i]
                pageUserLogin.link_Login().click()
                pageUserLogin.txtLoginUser().click()
                pageUserLogin.txtLoginUser().send_keys(userName)
                pageUserLogin.txtUserPWD().click()
                pageUserLogin.txtUserPWD().send_keys('Aarena888')
                pageUserLogin.txtVerifyCode().click()
                # TODO: Verify Code
                TestUtility.sleepTime(5)
                pageUserLogin.btnLogin().click()
                # 3: Open the target game





            # 4: Join this game
            # 5： logout this user


class adminUserTCs():

    ini_balance = 0
    promote_persent = 0
    falie_persent = 0

    faileline_points_LevelOne = 0
    promote_points_LevelOne = 0

    promote_points_L2 = 0
    faile_poinsts_L2 = 0

    promote_points_L3 = 0
    faile_poinsts_L3 = 0

    def self_configLevelOne():
        pageAdmin.confPanel().click()
        pageAdmin.btnAddLevel().click()
        pageAdmin.txtLveOneReward().click()
        # pageAdmin.txtLveOneReward().send_keys(sysConf.get(
        #     'ArenaChallengeCompetitionInfo').get('reward_points'))
        pageAdmin.txtLveOneReward().send_keys('0')
        # 'Set the competition faile value of Level1'
        pageAdmin.txtLevOneFaileLine().click()
        adminUserTCs.ini_balance = float(str(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('ini_balance')))

        adminUserTCs.falie_persent = float(str(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('faileline_persent')))
        adminUserTCs.faileline_points_LevelOne = str(adminUserTCs.ini_balance - adminUserTCs.ini_balance * adminUserTCs.falie_persent)
        pageAdmin.txtLevOneFaileLine().send_keys(adminUserTCs.faileline_points_LevelOne)

        # 'Set the promote value Level1'
        pageAdmin.txtLevOnePromoteLine().click()
        adminUserTCs.promote_persent = float(str(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('promote_persent')))
        adminUserTCs.promote_points_LevelOne = adminUserTCs.ini_balance + adminUserTCs.ini_balance * adminUserTCs.promote_persent
        pageAdmin.txtLevOnePromoteLine().send_keys(str(adminUserTCs.promote_points_LevelOne))

        # 'set the initial balance Level1'
        pageAdmin.txtLevOneIniBalance().click()
        pageAdmin.txtLevOneIniBalance().send_keys(str(adminUserTCs.ini_balance))

        # 'set the join permission Level1'
        pageAdmin.combResetPermission().click()
        pageAdmin.combResetPermission().send_keys(Keys.ARROW_DOWN)
        pageAdmin.combResetPermission().send_keys(Keys.ENTER)

        pageAdmin.btnConfirmAddLevel().click()

    def self_configLevelTwo():
        pageAdmin.txtLveTwoReward().click()
        pageAdmin.txtLveTwoReward().send_keys(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('reward_points'))
        # 'Set the competition faile value Level2'
        pageAdmin.txtLevTwoFaileLine().click()
        adminUserTCs.faile_poinsts_L2 = str(adminUserTCs.promote_points_LevelOne - adminUserTCs.promote_points_LevelOne * adminUserTCs.falie_persent)
        pageAdmin.txtLevTwoFaileLine().send_keys(adminUserTCs.faile_poinsts_L2)

        # 'Set the promote value 2'
        pageAdmin.txtLevTwoPromoteLine().click()
        adminUserTCs.promote_points_L2 = adminUserTCs.promote_points_LevelOne + adminUserTCs.promote_points_LevelOne * adminUserTCs.promote_persent
        pageAdmin.txtLevTwoPromoteLine().send_keys(str(adminUserTCs.promote_points_L2))

        # 'set the initial balance'
        pageAdmin.txtLevTwoIniBalance().click()
        pageAdmin.txtLevTwoIniBalance().send_keys(str(adminUserTCs.promote_points_LevelOne))

        # 'set the join permission'
        pageAdmin.combResetTwoPermission().click()
        pageAdmin.combResetTwoPermission().send_keys(Keys.ARROW_DOWN)
        pageAdmin.combResetTwoPermission().send_keys(Keys.ENTER)

        pageAdmin.btnConfirmTwoAddLevel().click()

    def self_configLevelThree():
        pageAdmin.txtLveThreeReward().click()
        pageAdmin.txtLveThreeReward().send_keys(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('reward_points'))
        # 'Set the competition faile value Level2'
        pageAdmin.txtLevThreeFaileLine().click()
        adminUserTCs.faile_poinsts_L3 = str(
            adminUserTCs.promote_points_L2 - adminUserTCs.promote_points_L2 * adminUserTCs.falie_persent)
        pageAdmin.txtLevThreeFaileLine().send_keys(adminUserTCs.faile_poinsts_L3)

        # 'Set the promote value 2'
        pageAdmin.txtLevThreePromoteLine().click()
        adminUserTCs.promote_points_L3 = adminUserTCs.promote_points_L2 + adminUserTCs.promote_points_L2 * adminUserTCs.promote_persent
        pageAdmin.txtLevThreePromoteLine().send_keys(str(adminUserTCs.promote_points_L3))

        # 'set the initial balance'
        pageAdmin.txtLevThreeIniBalance().click()
        pageAdmin.txtLevThreeIniBalance().send_keys(str(adminUserTCs.promote_points_L2))

        # 'set the join permission'
        pageAdmin.combResetThreePermission().click()
        pageAdmin.combResetThreePermission().send_keys(Keys.ARROW_DOWN)
        pageAdmin.combResetThreePermission().send_keys(Keys.ENTER)

        pageAdmin.btnConfirmThreeAddLevel().click()

    def tc_AdminAddCompetion():
        pageAdmin.changeAdminPortal()
        TestUtility.sleepTime(5)
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

        # 'Restall CompeDuration Value'
        TestUtility.sleepTime(3)
        pageAdmin.txtCompeDuration().click()
        TestUtility.sleepTime(1)
        pageAdmin.txtCompeDuration().send_keys(Keys.CONTROL, 'a')
        pageAdmin.txtCompeDuration().send_keys(sysConf.get(
            'ArenaChallengeCompetitionInfo').get('competition_duration'))

        pageAdmin.btnNextStep().click()
        '''
            Configure the competition the reward allocation.
        '''
        # 'Add level 2'
        adminUserTCs.self_configLevelOne()
        # 'Add level 2'
        pageAdmin.btnAddLevel().click()
        adminUserTCs.self_configLevelTwo()
        # 'Add level 3'
        pageAdmin.btnAddLevel().click()
        adminUserTCs.self_configLevelThree()

        #Close the level setting panel
        pageAdmin.closeLevelConfigureDialog().click()
        # Publish the new competition record
        pageAdmin.btnPublishCompe().click()
        # Conifrm the publish
        pageAdmin.btnConfirmPublish().click()








    def tc_addFund():
        pageAdmin.inconEnglish().click()
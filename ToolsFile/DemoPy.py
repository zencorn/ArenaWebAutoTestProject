from PageComponents.HtmlPageElements import *

class testCaseLib():
    def clickLogin():
        PageTest.linkLogin().click()
        PageRegist.linkForgetPWD().click()

testCaseLib.clickLogin()


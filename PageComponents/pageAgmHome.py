__author__ = 'JF'
from PageComponents.GUIElements import webTestDriver

class AgmHomePage():
    def regisClick(self,*dict):
        webTestDriver.linkRegister().click()

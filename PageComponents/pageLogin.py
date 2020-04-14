__author__ = 'JF'
from PageComponents.GUIElements import webTestDriver

class LoginPage():
    def regisClick(self,*dict):
        webTestDriver.linkRegister().click()
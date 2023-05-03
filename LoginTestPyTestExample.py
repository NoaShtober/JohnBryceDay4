import unittest

from PageObject.Pages.LoginPage import loginPage
from PageObject.Pages.WelcomePage import welcomePage
from PageObject.Tests.PageObjectBase import pageObjectBase


class loginTestPyTestExample(unittest.TestCase):

    def setUp(self):
        self.base = pageObjectBase()
        self.driver = self.base.selenium_start("https://www.saucedemo.com/")
        # \self.driver = self.base.selenium_start("https://demo.applitools.com/app.html")
        self.login_page = loginPage(self.driver)
        self.welcome_page = welcomePage(self.driver)
        # self.write_in_search()



    def teardown(self):
        self.base.selenium_end(self.driver)


    def test_login(self):
        self.login_page.login("standard_user", "secret_sauce")
        self.welcome_page.verify_title()


    def test_login_new_user(self):
        self.login_page.login("new_user", "secret_sauce")
        self.welcome_page.verify_title()


    def test_login_locked_user(self):
        self.login_page.login("problem_user", "secret_sauce")
        self.welcome_page.verify_title()

        '''
            def write_in_search(self):
                self.welcome_page.searchAplitools()

        '''

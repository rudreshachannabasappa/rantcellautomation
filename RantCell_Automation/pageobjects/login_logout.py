import time

from selenium.webdriver.common.by import By
from utils.library import library_utils as GL


class Log_In_Out:

    def __int__(self, driver):
        self.driver = driver

    def login(self, url, userid, password):

        try:
            link_login = [By.XPATH, "//a[normalize-space()='LOGIN']", "Login link"]
            textbox_username = (By.ID, "email", "Username")
            textbox_password = (By.ID, "password", "Password")
            button_login = (By.ID, "loginbutton", "Login button")
            link_Dashboard = (By.ID, "refreshDashboard", "Rant Cell")
            dropdown_dropdown_toggle = (By.XPATH, "//span[@class='ng-binding']//i[@class='caret']", "Drop Down Toggle")
            link_logout = (By.XPATH, "//a[normalize-space()='Logout']", "Logout")
            navigation_header = (By.XPATH, "//div[@class='navbar-header']//a[2]")
            dashboard = (By.XPATH, "//span[normalize-space()='Dashboard']")


            assert GL.launchbrowser(self, url, url)

            assert GL.click(self, link_login)

            time.sleep(5)

            assert (GL.inputtext(self, textbox_username, userid))

            time.sleep(2)

            assert (GL.inputtext(self, textbox_password, password))

            time.sleep(2)

            assert GL.click(self, button_login)

            time.sleep(5)

            assert GL.verifyelementispresent(self, dashboard, "Dashboard")

            time.sleep(5)

            # time.sleep(5)

            # assert GL.clickallure(self.link_login,"T")
            # assert True


        except Exception as e:
            assert False

    def logout(self):
        try:
            dropdown_dropdown_toggle = (By.XPATH, "//span[@class='ng-binding']//i[@class='caret']", "Drop Down Toggle")
            link_logout = (By.XPATH, "//a[normalize-space()='Logout']", "Logout")
            time.sleep(5)

            assert GL.click(self, dropdown_dropdown_toggle)

            time.sleep(5)

            assert GL.click(self, link_logout)


        except Exception as e:
            assert False

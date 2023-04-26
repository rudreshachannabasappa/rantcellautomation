import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObjects.loginPage import pageObjects

class LoginPage:

    def __init__(self, driver, username, password):
        self.driver = driver
        self.object = pageObjects()
        self.Login(username, password)

    def setUsername(self, username):
        WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(
            (By.ID, self.object.Username))).send_keys(username)
        # self.driver.find_element_by_id(self.object.Username).send_keys(username)

    def setPassword(self, password):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
            (By.ID, self.object.Password))).send_keys(password)
        # self.driver.find_element_by_id(self.object.Password).send_keys(password)

    def clickLogin(self):
        # self.driver.find_element_by_xpath(self.object.LOG_IN_BTN_ID).click()
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(
            (By.ID, self.object.LOG_IN_BTN_ID))).click()
        # self.driver.find_element_by_id(self.object.LOG_IN_BTN_ID).click()

    def Logout(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, self.object.LOGOUT_DROPDOWN_ARROW))).click()
        WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(
            (By.XPATH, self.object.LOGOUT))).click()
        # self.driver.find_element_by_xpath(self.object.LOGOUT).click()

    def Login(self, username, password):
        self.setUsername(username)
        self.setPassword(password)
        self.clickLogin()

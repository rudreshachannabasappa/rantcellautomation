import time
from time import sleep
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils import readexcel
from utils.library import library_utils as lb
from pageobjects.login_logout import Log_In_Out as GL
import os


class Test_Campaign_Driver:

    driver = None
    #global timeout
    #timeout= 10

    @pytest.mark.parametrize("device,campaign,environment,url,userid,password",
                             readexcel.readdata.fetch_camapaigns_enviroment(""))
    def test_campaign(self, setup, device, campaign, environment, url, userid, password):
        self.driver = setup

        # Fetch component based on the camapign "T001","T002" etc

        components = readexcel.readdata.fetch_components(campaign)

        # Login to RantCell Application

        GL.login(self, url, userid, password)

        # # Select device and perform campaign search

        # Click Android Test Data

        # time.sleep(5)
        #
        # AndroidTestData = [By.XPATH,"//span[text()='Android Test Data']","Android Test Data"]
        #
        # assert lb.clickec(self,AndroidTestData)
        #
        # time.sleep(5)
        #
        # ProTestData = [By.XPATH, "//span[text()='Pro TestData']", "Pro TestData"]
        #
        # assert lb.clickec(self, ProTestData)
        #
        # time.sleep(4)
        #
        # Variable_MobileDevice_Xpath = "//*[text()[contains(.,'" + str(device) + "')]]"
        #
        # assert lb.clickec(self, Variable_MobileDevice_Xpath)
        #
        # time.sleep(15)
        #
        #
        #
        # #
        # # print("performing campaign search:" + campaign)
        # #
        # # # Call Test Type - components - PingTest, Speed-Download,Speed-Upload.. etc...
        #
        # for x in components:
        #     print("Performing " + x + " test")

        GL.logout(self)






        # Close the browser





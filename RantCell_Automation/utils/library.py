import time
from datetime import datetime

import allure
from selenium.webdriver.common.by import By
from time import sleep
import logging
import os
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logger = logging.getLogger(__name__)

global timeout;
timeout = 10


class library_utils:

    def __init__(self, driver):
        self.driver = driver

    ################################################################-- LAUNCHBROWSER --##########################################################################################
    # Function:launchbrowser - Launches the browser and navigates to the URL
    # Parameters:
    #           url:https://preproductionpro.rantcell.com/
    #           title:https://preproductionpro.rantcell.com/
    # Revision History:

    def launchbrowser(self, url, title):
        try:
            with allure.step("Launch the browser and navigate to " + url):
                self.driver.get(url)
                time.sleep(2)
                self.driver.maximize_window()
                time.sleep(2)
                actualtitle = self.driver.current_url
                if actualtitle == title:
                    self.driver.get_screenshot_as_file("screenshot.png")
                    allure.attach.file("screenshot.png", name="URL" + actualtitle,
                                       attachment_type=allure.attachment_type.PNG)
                    time.sleep(2)
                    return True
                else:
                    self.driver.get_screenshot_as_file("screenshot.png")
                    allure.attach.file("screenshot.png", name="URL" + actualtitle,
                                       attachment_type=allure.attachment_type.PNG)
                    time.sleep(2)
                    return False
        except Exception as e:
            with allure.step("Launch the browser " + url):
                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name="URL", attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    ##################################################################################################################################################################################

    ##################################################################-- CLICK --##################################################################################################
    # Function:click - Clicks on particular element
    # Parameters:
    #           locators: (By.ID, self.textbox_username_id)
    # Revision History:

    def click(self, locators):
        try:
            locatortype = locators[0]
            locatorProperty = locators[1]
            elementname = locators[2]
            with allure.step("Click on " + elementname + " element"):
                self.driver.find_element(locatortype, locatorProperty).click()
                return True
        except Exception as e:
            with allure.step("Failed to click on " + elementname + "element"):
                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name=elementname, attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    def clickec(self, locators):
        try:
            elementname = locators[2]
            Locators = []
            Locators.append(locators[0])
            Locators.append(locators[1])

            with allure.step("Click on " + elementname + " element"):
                element = WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(Locators))
                element.click()
                return True
        except Exception as e:
            with allure.step("Failed to click on " + elementname + "element"):
                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name=elementname, attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    #####################################################################################################################################################################################

    #################################################################-- INPUTTEXT --###################################################################################
    # Function:inputtext - Enters the value in Text Edit Field
    # Parameters:
    #           locators: (By.ID, self.textbox_username_id)
    #           value   : eva@rantcell.com
    # Revision History:

    def inputtext(self, locators, value):
        try:
            locatortype = locators[0]
            locatorProperty = locators[1]
            elementname = locators[2]
            with allure.step("Enter " +  value + " in " + elementname + " edit field "):
                self.driver.find_element(locatortype, locatorProperty).send_keys(value)
                return True
        except Exception as e:
            with allure.step("Failed to enter the value in " + elementname + " text field element"):
                self.driver.get_screenshot_as_file("screenshot.png")
                allure.attach.file("screenshot.png", name=elementname, attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    ###################################################################################################################################################################################

    #####################################################################-- VERIFYELEMENTISPRESENT --############################################################################################
    # Function:verifyelementispresent - Verifies if a particular element is present or not
    # Parameters:
    #           locators: (By.XPATH, self.link_dashboard)
    #           elementName: Dashboard link
    # Revision History:

    def verifyelementispresent(self, Locators, elementName):
        try:
            with allure.step("Verify " + elementName + " element is present "):
                locatortype = Locators[0]
                locatorProperty = Locators[1]
                element = self.driver.find_element(locatortype, locatorProperty)
                # Verify if the element is present
                if element:
                    #self.takescreenshot(elementName)
                    self.driver.get_screenshot_as_file("screenshot.png")
                    allure.attach.file("screenshot.png", name=elementName, attachment_type=allure.attachment_type.PNG)
                    time.sleep(2)
                    return True
        except Exception as e:
            with allure.step("Failed to verify the " + elementName + " element "):
                self.takescreenshot(elementName)
                # self.driver.get_screenshot_as_file("screenshot.png")
                # allure.attach.file("screenshot.png", name=elementName, attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    ###############################################################################################################################################################

    ####################################################-- TAKESCREENSHOT --#######################################################################################
    # Function:verifyelementispresent - Verifies if a particular element is present or not
    # Parameters:
    #           elementName: textbox_username
    # Revision History:

    def takescreenshot(self, elementName):
        self.driver.get_screenshot_as_file("screenshot.png")
        allure.attach.file("screenshot.png", name=elementName, attachment_type=allure.attachment_type.PNG)

    #################################################################################################################################################################



#####################################################################-- VERIFYELEMENTISPRESENT --############################################################################################
    # Function:verifyelementispresent - Verifies if a particular element is present or not
    # Parameters:
    #           locators: (By.XPATH, self.link_dashboard)
    #           elementName: Dashboard link
    # Revision History:

    def verifyelementispresentEC(self, Locators, elementName):
        try:
            with allure.step("Verify " + elementName + " element is present "):
                locatortype = Locators[0]
                locatorProperty = Locators[1]

                element1 = WebDriverWait(self.driver, 10).until(EC._element_if_visible(Locators))

                element2 = self.driver.find_element(locatortype, locatorProperty)

                A_element_present = EC.presence_of_element_located((By.XPATH, "//span[text()='Android Test Data']"))
                WebDriverWait(self.driver, timeout).until(A_element_present)



                # Verify if the element is present
                if element:
                    #self.takescreenshot(elementName)
                    self.driver.get_screenshot_as_file("screenshot.png")
                    allure.attach.file("screenshot.png", name=elementName, attachment_type=allure.attachment_type.PNG)
                    time.sleep(2)
                    return True
        except Exception as e:
            with allure.step("Failed to verify the " + elementName + " element "):
                self.takescreenshot(elementName)
                # self.driver.get_screenshot_as_file("screenshot.png")
                # allure.attach.file("screenshot.png", name=elementName, attachment_type=allure.attachment_type.PNG)
                time.sleep(2)
                return False

    ###############################################################################################################################################################
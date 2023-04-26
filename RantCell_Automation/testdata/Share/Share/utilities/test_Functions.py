from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.dashboard import DashboardPageObjects
import time

class func:
    global timeout
    timeout = 8


    def __init__(self, driver, logger, data):

        self.driver = driver
        self.logger = logger
        self.data = data
        global dashbrdPgObj
        dashbrdPgObj = DashboardPageObjects()
        self.wait = WebDriverWait(self.driver, 10)

    def verify_dashboardKeyword(self):
        try:
            element_present = EC.presence_of_element_located(
                dashbrdPgObj.HOMEPAGE_DASHBOARD_KEYWORD_TEXT)
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            self.logger.error("  Timed out waiting for page to load  ")
            assert False

    def map_area(self):
        try:
            element_present = EC.presence_of_element_located(dashbrdPgObj.MAP_AREA)
            WebDriverWait(self.driver, timeout).until(element_present)
        except TimeoutException:
            self.logger.error("  Timed out waiting for page to load  ")

    def uncheck_listOfcampaign(self):
        List_of_Campaigns_checkBox = self.driver.find_element('xpath','//input[@type="checkbox"][@id="deSelectAll"]') # List of Campaigns CheckBox
        if (List_of_Campaigns_checkBox.is_selected()):
            List_of_Campaigns_checkBox.click()
        else:
            self.logger.error("  List of campaigns is already unchecked  ")


    def verify_Export_dropdown_button(self):
        try:
            time.sleep(2)
            Export_DropDown_btn = EC.presence_of_element_located(dashbrdPgObj.EXPORT_DROPDOWN_BUTTON)
            WebDriverWait(self.driver, timeout).until(Export_DropDown_btn).click()
        except TimeoutException:
            self.logger.error("  Unable to click on expand map  ")
            self.logger.error("  FAIL  : Unable to verify Expanded Map-View Page")

    def verify_map_presence(self):
        try:
            Map_btn = EC.presence_of_element_located(
                (By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Map")]]'))
            WebDriverWait(self.driver, timeout).until(Map_btn)
            self.driver.find_element(By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Map")]]').click()
            self.logger.warn("  PASS : Map Displayed  ")
        except TimeoutException:
            self.logger.error("  FAIL  : No Map Displayed")

    def verify_map_content(self):
        ele1 = self.driver.find_element(By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Map")]]')
        ele2 = self.driver.find_element(By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Satellite")]]')
        ele5 = self.driver.find_element(By.XPATH, '//h6[@class="box-title hidden-xs"][text()[contains(.,"Operator Comparison")]]')
        Nonele6 = self.driver.find_element(By.XPATH, '//h3[text()[contains(.,"No test data found. Please try different date and time range.")]]')
        if (Nonele6.is_displayed()):
            self.logger.error("    FAIL  : Unable to load Map. Map is not loaded for selected campaign  ")
        else:
            if (ele1.is_displayed()):
                if (ele2.is_displayed()):
                    if (ele5.is_displayed()):
                        self.logger.info("  PASS   : Map is loaded successfully")

    def click_on_MapBlob(self):
        time.sleep(2)
        Blob_OnMap = dashbrdPgObj.BLOB_ONMAP
        try:
            Data_Blob = EC.presence_of_element_located(Blob_OnMap)
            WebDriverWait(self.driver, timeout).until(Data_Blob).click()
            time.sleep(2)
        except TimeoutException:
            self.logger.error("  FAIL  : No Test data")

    def extract_MapBlob_data(self):
        Ping_Test_data_from_Map = '//div[@class ="info-window ng-scope"]'
        try:
            T_data = EC.presence_of_element_located((By.XPATH, Ping_Test_data_from_Map))
            WebDriverWait(self.driver, timeout).until(T_data)

            Element = self.driver.find_element(By.XPATH, Ping_Test_data_from_Map)
            var = Element.text
            self.logger.debug("\n\n" + "    Test Data from Map for    " + str(
                self.data["Types of Test"] + " - " + self.data["Classifier"]) + " :" + "\n\n"+var+"\n\n\n")
            Screenshots_name = "PASS__Test_data_from_map_is_displayed_for_"\
                               +str(self.data["Types of Test"]).replace("-","_").replace(" ", "_") \
                               +"___" + str(self.data["Classifier"]).replace("-","_").replace(" ", "_")
            self.logger.warn(Screenshots_name)
            self.driver.save_screenshot("../Screenshots/"+Screenshots_name)
        except TimeoutException:
            self.logger.error("  FAIL  : No Test data from Map for ")

    def validate_Mapextracted_TestData(self):
        time.sleep(2)
        MapsTestData_keys = self.driver.find_elements(By.XPATH, '//td[@class="option-name ng-binding"]')
        MapsTestData_values = self.driver.find_elements(By.XPATH, '//td[@class="option-value ng-binding"]')
        size = len(MapsTestData_keys)
        self.logger.info("No. of elements in Map-Tooltip : "+str(size))
        self.logger.info("\n\n")
        for i in range(size):
            # self.logger.info(str(MapsTestData_keys[i].text) +" = "+ str(MapsTestData_values[i].text))
            if str(MapsTestData_keys[i].text.lower()) == ("Operator Name").lower():
                # self.logger.info(len(str(MapsTestData_values[i].text)))
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn(
                        "" + "  PASS  : " + str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text))
                else:
                    self.logger.error("" + "FAIL: Operator Name is not displayed" + "")
            if str(MapsTestData_keys[i].text.lower()) == ("CellID/ECI").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn(
                        "" + "  PASS  : " + str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : CellID is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
            if str(MapsTestData_keys[i].text.lower()) == ("DATA").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn("" + "  PASS  : " + str(MapsTestData_keys[i].text) + " Type = " + str(
                        MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : Data Type is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
            if str(MapsTestData_keys[i].text.lower()) == ("NetworkType").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn(
                        "" + "  PASS  : " + str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : Network Type is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
            if str(MapsTestData_keys[i].text.lower()) == ("nrSSRSRP").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn("" + "  PASS  : " + str(MapsTestData_keys[i].text) + " Type = " + str(
                        MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : nrSSRSRP is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
            if str(MapsTestData_keys[i].text.lower()) == ("nrSSRSRQ").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn("" + "  PASS  : " + str(MapsTestData_keys[i].text) + " Type = " + str(
                        MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : nrSSRSRQ is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
            if str(MapsTestData_keys[i].text.lower()) == ("nrArfcn").lower():
                if str(MapsTestData_values[i].text.lower()) != "" and len(
                        str(MapsTestData_values[i].text)) >= 1 and str(MapsTestData_values[i].text.lower()) != "-":
                    self.logger.warn(
                        "" + "  PASS  : " + str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")
                else:
                    self.logger.error("" + "  FAIL  : nrArfcn/arfcn is empty/not displayed")
                    self.logger.error(str(MapsTestData_keys[i].text) + " = " + str(MapsTestData_values[i].text) + "")

    def extract_MapTableData(self):
        Ping_Test_data_from_Table = '//table[@class="table-condensed table-bordered table-hover table-striped ng-scope"]'
        try:
            Table_data = EC.presence_of_element_located((By.XPATH, Ping_Test_data_from_Table))
            WebDriverWait(self.driver, timeout).until(Table_data)

            Element = self.driver.find_element(By.XPATH, Ping_Test_data_from_Table)

            self.logger.debug("\n\n"+"Test Data from table for "+ str(self.data["Types of Test"]+" - "+self.data["Classifier"]) +" :"+"\n\n"+Element.text+"\n\n")
            # self.logger.info("\n\n"+Element.text+"\n\n")

            self.logger.warn("" + "  PASS   : Ping_Test_data_from_Table is Displayed" + "")
        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Test data from table" + "")

    def extract_graphPointData(self):
        time.sleep(2)
        Graph_Tootip = '//*[@id="chartContainer"]/div/div[@class="canvasjs-chart-tooltip"]'

        try:
            Graph_data = EC.presence_of_element_located((By.XPATH, Graph_Tootip))
            WebDriverWait(self.driver, timeout).until(Graph_data)

            Element = self.driver.find_element(By.XPATH, Graph_Tootip)

            self.logger.debug("\n\n" + "Test Data from Graph for "+ str(self.data["Types of Test"]+" - "+self.data["Classifier"]) +" :" + "\n\n"+Element.text+"\n\n")
            # self.logger.info("\n\n"+Element.text+"\n\n")

            self.logger.warn("" + "  PASS   : Test_data_from_Graph is Displayed" + "")
        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Test data from Graph" + "")

    def check_ifDeviceNameisPresent(self):
        time.sleep(2)
        a = 1
        try:
            # self.logger.info("Device Name : "+data["DeviceName"])
            DeviceName = str(self.data["DeviceName"])
        except:
            DeviceName = "Samsung SM-S908E"
        self.logger.info("Verify Device Name in Table View Loading")
        # hard-coded xpath for particular device named above [Samsung SM-S908E]
        col = self.driver.find_elements(By.XPATH, '//td[@class = "ng-binding"]')
        for key in col:
            # self.logger.info(key.text)
            if DeviceName in key.text:
                a = 0
                break

        if a == 0:
            self.logger.info(DeviceName + " is present in Table View Loading")
        else:
            self.logger.error("No! it is not present in Table View Loading")
            assert False

    def clickOnCampaignAndVerifyData(self):
        try:
            time.sleep(2)
            # hard-coded xpath for particular device named above [Samsung SM-S908E]
            A_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="loaderCamp"]/abbr/a'))
            WebDriverWait(self.driver, timeout).until(A_present).click()
            # self.driver.find_element(By.XPATH, '//*[@id="loaderCamp"]/abbr/a').click()
            # self.logger.info("Click the campaign in Popup view loading")
        except TimeoutException:
            self.logger.error("Unable to Click the campaign in Popup view loading")

        try:
            time.sleep(2)
            if (self.driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div').is_displayed()):
                self.logger.info("   Campaign Page is displayed, Successfully verified..!!!   ")

            B_present = EC.element_to_be_clickable((By.XPATH, '//*[@id="loaderCamp"]/abbr/a'))
            WebDriverWait(self.driver, timeout).until(B_present)
            self.driver.find_element(By.XPATH, '//*[@id="myModal"]/div/div/div[5]/button').click()
            self.logger.warn(" PASS : " + "Campaign Pop-up Home Page is displayed" + "    ")
        except TimeoutException:
            self.logger.error("Unable to display Pop-up Home Page")

    def downloadReport(self):

        from selenium.webdriver.support.ui import Select
        time.sleep(2)
        ExportSelect = '//*[@id="tableView"]/div[1]/div/select'
        # CampaignTable = '//div[@class='div-table-content']'
        select_fr = Select(self.driver.find_element(By.XPATH, ExportSelect))
        select_fr.select_by_index(1)
        select_fr.select_by_index(0)
        # select_fr.select_by_index(2)
        self.logger.info("" + "File Downloaded Successfully" + "")

    def checkDownloadedReportAndDelete(self):
        time.sleep(2)
        import getpass, glob, os

        # Get downloads
        list_of_files = glob.glob("C:\\Users\\{}\\Downloads\\*".format(getpass.getuser()))
        latest_file = max(list_of_files, key=os.path.getctime)
        # self.logger.info("")
        self.logger.info(latest_file)
        # self.logger.info("")

        import csv
        newfolderpath = latest_file
        with open(newfolderpath, 'r') as file:
            csvreader = csv.reader(file)
            header = next(csvreader)
            for row in csvreader:
                if row != []:
                    self.logger.warn("\n\n  PASS : File Downloaded is not empty\n")
                    self.logger.info("\n\nData is present as below : \n\n"+str(row)+"\n\n\n")
                    # self.logger.info(row)
                    # self.logger.info("\n\n\n")
                else:
                    self.logger.error("  FAIL  : File Downloaded is empty")

        if str(latest_file).endswith('.csv'):
            os.remove(latest_file)
            self.logger.error("\n\n\nDeleted the file successfully from : " + "" + latest_file + "\n\n")
        elif str(latest_file).lower().endswith('.csv'):
            os.remove(latest_file)
            self.logger.error("\n\n\nDeleted the file successfully from : " + "" + latest_file + "\n\n")
        else:
            self.logger.error("  FAIL  : Unable to download file")
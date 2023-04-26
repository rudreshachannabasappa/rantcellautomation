from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from pageObjects.dashboard import DashboardPageObjects
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
import time

class nav:
    global timeout
    timeout = 15

    def __init__(self, driver, logger, test_data):

        self.driver = driver
        self.logger = logger
        self.data = test_data
        self.dashboard_page_objects = DashboardPageObjects()
        self.wait = WebDriverWait(self.driver, 10)

    def fromDevice_selectTestCase(self):

        # Link="Android Test Data"
        try:
            A_element_present = EC.presence_of_element_located((By.XPATH, "//span[text()='Android Test Data']"))
            WebDriverWait(self.driver, timeout).until(A_element_present)
            self.driver.find_element("xpath", "//span[text()='Android Test Data']").click()
        except TimeoutException:
            self.logger.error("Unable to find the link - Android Test Data on RantCell | Dashboard")

        # Link="Android Test Data"
        try:
            time.sleep(2)
            B_element_present = EC.presence_of_element_located((By.XPATH, "//span[text()='Pro TestData']"))
            WebDriverWait(self.driver, timeout).until(B_element_present)
            self.driver.find_element("xpath", "//span[text()='Pro TestData']").click()
        except TimeoutException:
            self.logger.error("Unable to find the link - Pro TestData on RantCell | Dashboard")

        Variable_MobileDevice_Xpath = "//*[text()[contains(.,'"+str(self.data["Device"])+"')]]"
        try:
            time.sleep(2)
            C_element_present = EC.presence_of_element_located((By.XPATH, Variable_MobileDevice_Xpath))
            WebDriverWait(self.driver, timeout).until(C_element_present)
            self.driver.find_element("xpath", Variable_MobileDevice_Xpath).click()

        except TimeoutException:
            self.logger.error("Unable to find the link - Variable_MobileDevice on RantCell | Dashboard")
            assert False

        Show_More = "//a[text()[contains(.,'Show More')]]"
        try:
            time.sleep(2)
            if self.driver.find_element("xpath", Show_More).is_displayed():
                E_element_present = EC.presence_of_element_located((By.XPATH, Show_More))
                WebDriverWait(self.driver, timeout).until(E_element_present)
                self.driver.find_element("xpath", Show_More).click()

        except TimeoutException:
            self.logger.error("Unable to find the Show_More")

        time.sleep(2)
        PingOption_AndriodTestData = "//span[text()[contains(.,'"+self.data["Classifier"]+"')]]"
        element = self.driver.find_element("xpath", PingOption_AndriodTestData)
        try:
            time.sleep(2)
            D_element_present = EC.element_to_be_clickable((By.XPATH, PingOption_AndriodTestData))
            WebDriverWait(self.driver, timeout).until(D_element_present)
            self.driver.find_element("xpath", PingOption_AndriodTestData).click()
            self.logger.info("Clicked on 'PingOption[Andriod TestData -> ProTest data -> Device -> "+str(self.data["Classifier"])+"'")
        except TimeoutException:
            self.logger.error("Unable to find the link - Ping on RantCell | Dashboard")
            self.logger.error("Trying.............. Again!!!!")
            if EC._element_if_visible(element):
                element.click()

            self.driver.find_element("xpath", Variable_MobileDevice_Xpath).click()
            D_element_present = EC.element_to_be_clickable((By.XPATH, PingOption_AndriodTestData))
            WebDriverWait(self.driver, timeout).until(D_element_present)
            self.driver.find_element("xpath", PingOption_AndriodTestData).click()
            self.logger.info("Clicked on 'PingOption[Andriod TestData -> ProTest data -> Device -> "+str(self.data["Classifier"])+"'")

    def expand_mapView(self):
        try:
            time.sleep(2)
            Expand_Map = EC.presence_of_element_located((By.XPATH, '//a[@id="exapandMap"]'))
            WebDriverWait(self.driver, timeout).until(Expand_Map)
            self.driver.find_element("xpath", '//a[@id="exapandMap"]').click()

        except TimeoutException:
            self.logger.error("Unable to click on expand map")

    def select_testTypeFromDropdown(self, test, driver):
        try:
            # self.driver = driver
            time.sleep(1)
            Export_DropDown_btn = EC.presence_of_element_located((By.ID, 'exportselectionBox'))
            WebDriverWait(driver, timeout).until(Export_DropDown_btn)
            # driver.find_element(By.ID, 'exportselectionBox').click()
            # self.logger.info("" + "  PASS  : Successfully verified 'Export button' on Expanded Map-View Page" + "")
        except TimeoutException:
            # self.logger.error("" + "Unable to click on expand map")
            # self.logger.error("  FAIL  : Unable to verify Expanded Map-View Page" + "")
            pass

        time.sleep(1)

        # test = self.data["Types of Test"]
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,
                                                                        '(//*[@id="mainContent"]//a[@role="button"])[position()=1]'))).click()
        driver.implicitly_wait(10)

        txt = []
        if "Call Test" in test:
            txt = ["Call Test", "Call Test"]
        if "Call Test_FC" in test:
            txt = ["Call Test", "Failed Calls"]
        if "Ping Test" in test:
            txt = ["Ping Test"]
        if "WebTest" in test:
            txt = ["WebTest"]
        if "Speed Test_DL" in test or "Speed Test-DL" in test:
            txt = ["Speed Test", "Download Test"]
        if "Speed Test_UL" in test or "Speed Test-UL" in test:
            txt = ["Speed Test", "Upload Test"]
        if "Iperf Test_TCP_DL" in test:
            txt = ["Iperf Test", "TCPiPerfDL"]
        if "Iperf Test_TCP_UL" in test:
            txt = ["Iperf Test", "TCPiPerfUL"]
        if "Iperf Test_UDP_DL" in test:
            txt = ["Iperf Test", "UDPiPerfDL"]
        if "Iperf Test_UDP_UL" in test:
            txt = ["Iperf Test", "UDPiPerfUL"]
        if "HTTP Test_DL" in test:
            txt = ["Http Test", "Http Download Test"]
        if "HTTP Test_UL" in test:
            txt = ["Http Test", "Http Upload Test"]
        if "Sms Test_RCV" in test:
            txt = ["Sms Test", "Received Sms"]
        if "Sms Test_FL" in test:
            txt = ["Sms Test", "Failed Sms"]
        if "Stream Test" in test:
            txt = ["Stream Test"]
        # if "Sms Test" in test:
        #     txt = ["Sms Test", "Sent Sms"]
        if "RSSI/RSCP" in test:
            txt = ["Coverage Map", "RSSI/RSCP"]
        if "RSRP" in test:
            txt = ["Coverage Map", "RSRP"]
        if "RSRQ" in test:
            txt = ["Coverage Map", "RSRQ"]
        if "nrSsRsrp" in test or "nrSSRSRP" in test:
            txt = ["Coverage Map", "nrSsRsrp"]
        if "nrSsRsrq" in test or "nrSSRSRQ" in test:
            txt = ["Coverage Map", "nrSsRsrq"]
        if "ECNO_3G" in test:
            txt = ["Coverage Map", "ECNO_3G"]
        if "BCCH_arfcn" in test:
            txt = ["Coverage Map", "BCCH_arfcn"]
        if "PSC" in test:
            txt = ["Coverage Map", "PSC"]
        if "PCI" in test:
            txt = ["Coverage Map", "PCI"]
        if "lteSNR" in test:
            txt = ["Coverage Map", "lteSNR"]
        if "Data Type" in test:
            txt = ["Coverage Map", "Data Type"]
        if "Network Type" in test:
            txt = ["Coverage Map", "Network Type"]
        if "Arfcn" in test or "arfcn" in test:
            txt = ["Coverage Map", "Arfcn"]
        if "CellID View" in test or "cellid View" in test:
            txt = ["Coverage Map", "CellID View"]

        for set_txt in txt:
            dropdown_select = '//*[@id="mainContent"]//a[@class="ng-binding" and text()[contains(.,"' + str(
                set_txt) + '")]]'
            Export_DropDown_btn = EC.presence_of_element_located((By.XPATH, dropdown_select))
            WebDriverWait(driver, timeout).until(Export_DropDown_btn)
            driver.find_element(By.XPATH, dropdown_select).click()

        time.sleep(10)

        try:
            _Blob_OnMap = '//div[@role="button"]/img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]'
            __Blob_OnMap = EC.presence_of_element_located((By.XPATH, _Blob_OnMap))
            WebDriverWait(driver, timeout).until(__Blob_OnMap)
            driver.find_element(By.XPATH, _Blob_OnMap).click()
            time.sleep(2)
        except TimeoutException:
            self.logger.debug("Try did not work")
            _Blob_OnMap_1 = '//*[@id="gmaps-marker"]/div/div/div[2]/div[2]/div/div[3]/div[5]/img'
            __Blob_OnMap_1 = EC.presence_of_element_located((By.XPATH, _Blob_OnMap_1))
            WebDriverWait(driver, timeout).until(__Blob_OnMap_1)
            driver.find_element(By.XPATH, _Blob_OnMap_1).click()
            self.logger.debug("Except")
            time.sleep(2)

        Ping_Test_data_from_Map = '//div[@class ="info-window ng-scope"]'

        try:
            T_data = EC.presence_of_element_located((By.XPATH, Ping_Test_data_from_Map))
            WebDriverWait(driver, timeout).until(T_data)

            Element = driver.find_element(By.XPATH, Ping_Test_data_from_Map)
            var = Element.text
            self.logger.debug(var)
            #self.logger.debug("\n\n" + "    Test Data from Map for    " + str(
                # self.data["Types of Test"] + " - " + self.data["Classifier"]) + " :" + "\n\n" + Element.text + "\n\n")
            #self.logger.warn("  PASS   : Test data from map is displayed    ")
        except TimeoutException:
            #self.logger.error("  FAIL  : No Test data from Map")
            pass

########################################################################################################################

    def _select_testTypeFromDropdown(self):
        try:
            time.sleep(1)
            Export_DropDown_btn = EC.presence_of_element_located((By.ID, 'exportselectionBox'))
            WebDriverWait(self.driver, timeout).until(Export_DropDown_btn)
            self.driver.find_element(By.ID, 'exportselectionBox').click()
            self.logger.info("" + "  PASS  : Successfully verified 'Export button' on Expanded Map-View Page" + "")
        except TimeoutException:
            self.logger.error("" + "Unable to click on expand map")
            self.logger.error("  FAIL  : Unable to verify Expanded Map-View Page" + "")
            pass

        time.sleep(1)

        FstDropDwn = '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul'
        element = self.driver.find_element(By.XPATH, FstDropDwn)
        text = element.get_attribute("textContent")

        import re

        text = re.sub(' +', '', text).strip()
        text = re.sub('\n+', ' ', text).strip()
        # self.logger.debug(text)
        cleaned_text = re.sub('\s+', '', text).strip()

        for key in self.data.keys():
            ctext = re.sub(' +', '', key).strip().lower()
            if ctext in cleaned_text.lower():
                # self.logger.debug("Exp : " + key)
                test = key

                # test = self.data["Types of Test"]
                # self.logger.info("Types of Test : " +test)
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((By.XPATH,
                    '(//*[@id="mainContent"]//a[@role="button"])[position()=1]'))).click()
                self.driver.implicitly_wait(10)
                self.logger.info(test)
                txt = []
                if "Call Test" in test or "Call test" in test:
                    try:
                        txt = ["Call Test"]
                        self.driver.find_element(By.XPATH,
                                                 '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul/li[1]/ul/li[1]/a').click()
                    except:
                        self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul/li[1]/a[2]').cick()
                        time.sleep(2)
                        self.driver.find_element(By.XPATH, '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul/li[1]/ul/li[1]/a').click()
                if "Call Test_FC" in test:
                    txt = ["Call Test", "Failed Calls"]
                if "Ping Test" in test:
                    txt = ["Ping Test"]
                if "WebTest" in test or "Web test" in test:
                    txt = ["WebTest"]
                if "Speed Test_DL" in test or "Speed Test-DL" in test or "Download Test" in test:
                    txt = ["Speed Test", "Download Test"]
                if "Speed Test_UL" in test or "Speed Test-UL" in test or "Upload test" in test:
                    txt = ["Speed Test", "Upload Test"]
                if "Iperf Test_TCP_DL" in test:
                    txt = ["Iperf Test", "TCPiPerfDL"]
                if "Iperf Test_TCP_UL" in test:
                    txt = ["Iperf Test", "TCPiPerfUL"]
                if "Iperf Test_UDP_DL" in test:
                    txt = ["Iperf Test", "UDPiPerfDL"]
                if "Iperf Test_UDP_UL" in test:
                    txt = ["Iperf Test", "UDPiPerfUL"]
                if "HTTP Test_DL" in test:
                    txt = ["Http Test", "Http Download Test"]
                if "HTTP Test_UL" in test:
                    txt = ["Http Test", "Http Upload Test"]
                if "Sms Test_RCV" in test:
                    txt = ["Sms Test", "Received Sms"]
                if "Sms Test_FL" in test:
                    txt = ["Sms Test", "Failed Sms"]
                if "Stream Test" in test:
                    txt = ["Stream Test"]
                if "Sms Test" in test or "Sent SMS" in test:
                    txt = ["Sms Test", "Sent Sms"]
                if "RSSI/RSCP" in test:
                    txt = ["Coverage Map", "RSSI/RSCP"]
                if "RSRP" in test:
                    txt = ["Coverage Map", "RSRP"]
                if "RSRQ" in test:
                    txt = ["Coverage Map", "RSRQ"]
                if "nrSsRsrp" in test or "nrSSRSRP" in test:
                    txt = ["Coverage Map", "nrSsRsrp"]
                if "nrSsRsrq" in test or "nrSSRSRQ" in test:
                    txt = ["Coverage Map", "nrSsRsrq"]
                if "ECNO_3G" in test:
                    txt = ["Coverage Map", "ECNO_3G"]
                if "BCCH_arfcn" in test:
                    txt = ["Coverage Map", "BCCH_arfcn"]
                if "PSC" in test:
                    txt = ["Coverage Map", "PSC"]
                if "PCI" in test:
                    txt = ["Coverage Map", "PCI"]
                if "lteSNR" in test:
                    txt = ["Coverage Map", "lteSNR"]
                if "Data Type" in test:
                    txt = ["Coverage Map", "Data Type"]
                if "Network Type" in test:
                    txt = ["Coverage Map", "Network Type"]
                if "Arfcn" in test or "arfcn" in test:
                    txt = ["Coverage Map", "Arfcn"]
                if "CellID View" in test or "cellid View" in test:
                    txt = ["Coverage Map", "CellID View"]


                for set_txt in txt:
                    dropdown_select = '//*[@id="mainContent"]//a[@class="ng-binding" and text()[contains(.,"' + str(
                        set_txt) + '")]]'
                    Export_DropDown_btn = EC.presence_of_element_located((By.XPATH, dropdown_select))
                    WebDriverWait(self.driver, timeout).until(Export_DropDown_btn)
                    self.driver.find_element(By.XPATH, dropdown_select).click()

                time.sleep(2)

                try:
                    from selenium.webdriver.common.alert import Alert
                    # Check if an alert pop-up is present
                    alert = Alert(self.driver)
                    alert_text = alert.text

                    # Accept the alert if present
                    alert.accept()
                    self.logger.error(f"Accepted alert with message: {alert_text}")
                    self.logger.error(f"There is no data for : {test}")
                    self.logger.info(f"\n\n   *************** Map data for \"{test}\" ends here ***************  \n\n\n")
                except:
                    # Continue with the execution if no alert is present
                    # self.logger.info("No alert pop-up found")

                    try:
                        Map_marker = '//*[@id="gmaps-marker"]/div/div/div[2]/div[2]/div/div[3]/div/div'
                        GMap_marker = EC.presence_of_element_located((By.XPATH, Map_marker))
                        WebDriverWait(self.driver, 2).until(GMap_marker)
                        self.driver.find_element(By.XPATH, Map_marker).click()
                        time.sleep(2)
                    except:
                        pass

                    # click the button until it is displayed on the screen
                    while not self.driver.find_element(By.XPATH,
                                                       '//div[@role="button"]/img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]').is_displayed():
                        # zoom_out = self.driver.find_element(By.XPATH,
                        #                                     '(//*[@id="gmaps-marker"]//button[@class="gm-control-active"])[position()=4]')
                        zoom_out = self.driver.find_element(By.XPATH,
                                                            '//*[@id="gmaps-marker"]/div/div/div[13]/div/div[3]/div/button[2]')
                        zoom_out.click()
                        time.sleep(2)
                        # find the element using xpath
                        element = self.driver.find_element(By.XPATH, '//*[@id="getZoomLevel"]')
                        # self.logger.info(element.text)
                        # get the text of the element
                        if "Zoom : 2" in str(element.text):
                            break

                    try:
                        _Blob_OnMap = '//div[@role="button"]/img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]'
                        blobs = self.driver.find_elements(By.XPATH, _Blob_OnMap)
                        # self.logger.info("Number of blobs : " + str(len(blobs)))

                        for blob in blobs:
                            if blob.is_displayed():
                                action = ActionChains(self.driver)
                                action.move_to_element(blob).click().perform()
                                break

                        time.sleep(2)
                    except Exception as e:
                        self.logger.info(str(e))

                        # self.logger.debug("Try did not work")
                        # _Blob_OnMap = '//div[@role="button"]/img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]'
                        # elements  = self.driver.find_elements(By.XPATH, _Blob_OnMap).click()
                        # for element in elements :
                        #     element.click()
                        # time.sleep(2)
                        pass

                    Ping_Test_data_from_Map = '//div[@class ="info-window ng-scope"]'

                    try:
                        Ping_Test_data_from_Map = '//div[@class ="info-window ng-scope"]'
                        try:
                            T_data = EC.presence_of_element_located((By.XPATH, Ping_Test_data_from_Map))
                            WebDriverWait(self.driver, timeout).until(T_data)

                            Element = self.driver.find_element(By.XPATH, Ping_Test_data_from_Map)
                            var = Element.text
                            self.logger.debug("\n\n" + "    Test Data from Map for    " + str(
                                self.data["Types of Test"] + " - " + self.data[
                                    "Classifier"]) + " :" + "\n\n" + var + "\n\n\n")
                            Screenshots_name = "PASS__Test_data_from_map_is_displayed_for_" \
                                               + str(self.data["Types of Test"]).replace("-", "_").replace(" ", "_") \
                                               + "_" + str(self.data["Classifier"]).replace("-", "_").replace(" ", "_") + "___" \
                                               + str(test).replace("-", "_").replace(" ", "_") +".png"
                            self.logger.warn(str(Screenshots_name).replace(".png",""))
                            self.driver.save_screenshot("../Screenshots/" + Screenshots_name)

                            # Find the driver element
                            driver_element = self.driver.find_element(By.XPATH, '//div[@class ="info-window ng-scope"]')

                            # Calculate the x and y offsets to click at a specific point
                            offset_x = 12
                            offset_y = 337

                            # Calculate the absolute x and y coordinates
                            abs_x = driver_element.location['x'] + offset_x
                            abs_y = driver_element.location['y'] + offset_y

                            # Create an ActionChains object
                            actions = ActionChains(self.driver)

                            # Move the mouse to the driver element
                            actions.move_to_element(driver_element)

                            # Move the mouse to the specified offset point
                            actions.move_by_offset(offset_x, offset_y).double_click().perform()
                            # time.sleep(5)
                            # actions.move_to_element_with_offset(driver_element, offset_x, offset_y).double_click().perform()
                            # time.sleep(5)
                            # self.driver.save_screenshot("../Screenshots/" + str(Screenshots_name).replace(".png","_1.png"))
                            time.sleep(5)

                        except TimeoutException:
                            self.logger.error("  FAIL  : No Test data from Map for ")
                    except TimeoutException:
                        self.logger.error("  FAIL  : No Test data from Map")
                        pass
                    self.logger.info(f"\n\n   *************** Map data \"{test}\" ends here ***************  \n\n\n")

########################################################################################################################

    def select_testTypeFromDropdown_UL(self):
        try:
            time.sleep(3)
            Export_DropDown_btn = EC.presence_of_element_located((By.ID, 'exportselectionBox'))
            WebDriverWait(self.driver, timeout).until(Export_DropDown_btn)
            self.driver.find_element(By.ID, 'exportselectionBox').click()
            self.logger.info("" + "  PASS  : Successfully verified 'Export button' on Expanded Map-View Page" + "")
        except TimeoutException:
            self.logger.error("" + "Unable to click on expand map")
            self.logger.error("  FAIL  : Unable to verify Expanded Map-View Page" + "")

        time.sleep(2)
        Campaigns_dropdown = '//*[@id="mainContent"]/div[1]/div/div[1]/div/a[1]/i'
        try:
            Campaigns_dropdown_btn = EC.presence_of_element_located((By.XPATH, Campaigns_dropdown))
            WebDriverWait(self.driver, timeout).until(Campaigns_dropdown_btn)
            self.driver.find_element(By.XPATH, Campaigns_dropdown).click()
        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Campaigns_dropdown Displayed" + "")

        time.sleep(2)
        Speedtest_dropdown = '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul/li[4]/a[2]'
        try:
            Speedtest_dropdown_btn = EC.presence_of_element_located((By.XPATH, Speedtest_dropdown))
            WebDriverWait(self.driver, timeout).until(Speedtest_dropdown_btn)
            self.driver.find_element(By.XPATH, Speedtest_dropdown).click()

        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Speedtest_dropdown Displayed" + "")

        time.sleep(2)
        Speedtest_dropdown_UL = '//*[@id="mainContent"]/div[1]/div/div[1]/div/ul/li[4]/ul/li[2]/a'
        try:
            Speedtest_dropdown_DL_btn = EC.presence_of_element_located((By.XPATH, Speedtest_dropdown_UL))
            WebDriverWait(self.driver, timeout).until(Speedtest_dropdown_DL_btn)
            self.driver.find_element(By.XPATH, Speedtest_dropdown_UL).click()

        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Speedtest_dropdown_DL Displayed" + "")

    def click_closeButton(self):
        try:
            time.sleep(2)
            closeFullTableView = EC.presence_of_element_located((By.ID, 'closeFullTableView'))
            WebDriverWait(self.driver, timeout).until(closeFullTableView)
            self.driver.find_element(By.ID, 'closeFullTableView').click()

        except TimeoutException:
            self.logger.error("Unable to close map-view")


    def expand_graphView(self):
        ExpGraph = '//*[@id="fullview"]/button[@class="btn btn-box-tool btn-sm btn-default pull-right"]'
        try:
            time.sleep(2)
            expand_GraphView = EC.presence_of_element_located((By.XPATH, ExpGraph))
            WebDriverWait(self.driver, timeout).until(expand_GraphView)
            self.driver.find_element(By.XPATH, ExpGraph).click()

        except TimeoutException:
            self.logger.error("Unable to expand graph-view")

    def select_SpeedTest_fromDropdown(self):
        time.sleep(2)
        Campaigns_dropdown = '//*[@id="graphwindow"]/div/div/div[1]/div/button'
        try:
            Campaigns_dropdown_btn = EC.presence_of_element_located((By.XPATH, Campaigns_dropdown))
            WebDriverWait(self.driver, timeout).until(Campaigns_dropdown_btn)
            self.driver.find_element(By.XPATH, Campaigns_dropdown).click()

        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Campaigns_dropdown Displayed" + "")

        time.sleep(2)
        Speedtest_dropdown = '//*[@id="graphwindow"]/div/div/div[1]/div/ul/li[1]/a'
        try:
            Speedtest_dropdown_btn = EC.presence_of_element_located((By.XPATH, Speedtest_dropdown))
            WebDriverWait(self.driver, timeout).until(Speedtest_dropdown_btn)
            self.driver.find_element(By.XPATH, Speedtest_dropdown).click()

        except TimeoutException:
            self.logger.error("" + "  FAIL  : No Speedtest_dropdown Displayed" + "")

    def hoverOver_graphPoint(self):

        Graph = '//*[@id="chartContainer"]/div/canvas[2]'
        try:
            time.sleep(2)
            Actual_GraphView = EC.presence_of_element_located((By.XPATH, Graph))
            WebDriverWait(self.driver, timeout).until(Actual_GraphView)
        except TimeoutException:
            self.logger.error("Unable to view graph")

        time.sleep(2)
        from selenium import webdriver
        action = webdriver.ActionChains(self.driver)
        elm = self.driver.find_element(By.XPATH, Graph)
        action.move_to_element(elm).perform()

    def close_graphView(self):
        try:
            time.sleep(2)
            closeFullTableView = EC.presence_of_element_located((By.ID, 'closeFullTableView'))
            WebDriverWait(self.driver, timeout).until(closeFullTableView)
            self.driver.find_element(By.ID, 'closeFullTableView').click()

        except TimeoutException:
            self.logger.error("Unable to close Graph-view")


    def expand_tableViewAndNavigatebackDashboard(self):
        DataTable_Expand = '//*[@id="expandTableview"]/button'
        DataTable_Expanded_DataView = '//select[@ng-change="handleCSVall(whichoptSelected)"]'
        try:
            time.sleep(2)
            A_A = EC.element_to_be_clickable((By.XPATH, DataTable_Expand))
            WebDriverWait(self.driver, timeout).until(A_A)
            self.driver.find_element(By.XPATH, DataTable_Expand).click()

        except TimeoutException:
            self.logger.error("Unable to expand Campaign")

        time.sleep(3)
        self.driver.execute_script("window.history.go(-1)")
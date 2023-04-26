from pageObjects.dashboard import DashboardPageObjects
from utilities.test_Functions import func
from utilities._Navigations import nav

class speedtest_DL:

    
    def __init__(self, driver, logger, test_data):
        self.driver = driver
        self.logger = logger
        self.data = test_data
        self.dashboard_page_objects = DashboardPageObjects()
        self.page = func(self.driver, self.logger, self.data)
        self.navigate = nav(self.driver, self.logger, self.data)
        self.TC002()

    def TC002(self):
        try:
            self.page.verify_dashboardKeyword()
            self.page.map_area()
            self.page.uncheck_listOfcampaign()
            self.navigate.fromDevice_selectTestCase()
            self.navigate.expand_mapView()
            self.page.verify_Export_dropdown_button()
            self.page.verify_map_presence()
            self.page.verify_map_content()

            # self.logger.info("------------------------------------------------------------------------------------------")
            # self.logger.info("Step 3 : Based on Classifier map view to be loaded to get below data ")
            # self.logger.info("               ||")
            # self.logger.info("               |_=======> Reading  the data from Map View's Data Point present")

            self.navigate._select_testTypeFromDropdown()
            self.page.extract_MapTableData()
            self.navigate.click_closeButton()

            # self.logger.info("")
            # self.logger.info("------------------------------------------------------------------------------------------")
            # self.logger.info("Step 4 : Based on Classifier graph view to be loaded to get below data")
            # self.logger.info("               ||")
            # self.logger.info("               |_=======> Reading  the data from graph View's Data Point present")
            # self.logger.info("")

            self.navigate.expand_graphView()
            self.navigate.select_SpeedTest_fromDropdown()
            self.navigate.hoverOver_graphPoint()
            self.page.extract_graphPointData()
            self.navigate.close_graphView()
        
            # self.logger.info("------------------------------------------------------------------------------------------")
            # self.logger.info("Step 5 : Based on Classifier export to be downloaded and checked for")
            # self.logger.info("               ||")
            # self.logger.info("               |_=======> Download is happening and Data is present or not")
            # self.logger.info("")

            self.navigate.expand_tableViewAndNavigatebackDashboard()
            self.page.check_ifDeviceNameisPresent()
            self.page.clickOnCampaignAndVerifyData()
            self.page.downloadReport()
            self.page.checkDownloadedReportAndDelete()

        
            self.logger.info("")
            self.logger.critical(
                "\n\n" + "------------------------------------END------------------------------------------------------" + "\n\n")
            return 0
        except:
            self.logger.error("Unable to perform speed test")















        # finally:
        #     self.driver.quit()

# driver = webdriver.Chrome('C:\\Users\\Lenovo UTH-UK\\Downloads\\chromedriver_win32 (2)\\chromedriver.exe')
# driver.get('https://preproductionpro.rantcell.com/pages/dashboard.html#/login')
# driver.maximize_window()
# from utilities.businessFunction.Login import LoginPage
# LoginPage(driver, "eva@rantcell.com", 'eva@2023')
# pingtest(driver)
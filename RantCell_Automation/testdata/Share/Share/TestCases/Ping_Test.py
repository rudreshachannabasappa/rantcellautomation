from pageObjects.dashboard import DashboardPageObjects
from utilities.test_Functions import func
from utilities._Navigations import nav

class pingtest:

    def __init__(self, driver, logger, test_data):
        self.driver = driver
        self.logger = logger
        self.data = test_data
        self.dashboard_page_objects = DashboardPageObjects()
        self.page = func(self.driver, self.logger, self.data)
        self.navigate = nav(self.driver, self.logger, self.data)
        self.TC001()


    def TC001(self):
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

            # self.page.click_on_MapBlob()
            # MapData = self.page.extract_MapBlob_data()
            # self.page.validate_Mapextracted_TestData()
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
            self.logger.critical("\n\n"+"------------------------------------END------------------------------------------------------"+"\n\n")
            return 0
        except:
            self.logger.info("Unable to perform ping test")
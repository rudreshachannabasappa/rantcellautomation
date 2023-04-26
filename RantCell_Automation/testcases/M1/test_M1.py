import pytest

from pageobjects.login_logout import Log_In_Out as GL
from utils import readexcel


class Test_Campaign_Driver:
    driver = None

    @pytest.mark.parametrize("device,campaign,environment,url,userid,password",
                             readexcel.readdata.fetch_camapaigns_enviroment("T004"))
    def test_campaign(self, setup, device, campaign, environment, url, userid, password):
        self.driver = setup

        # Fetch component based on the camapign "T001","T002" etc

        components = readexcel.readdata.fetch_components(campaign)

        # Login to RantCell Application

        GL.login(self, url, userid, password)

        # # Select device and perform campaign search
        #
        # print("performing campaign search:" + campaign)
        #
        # # Call Test Type - components - PingTest, Speed-Download,Speed-Upload.. etc...

        for x in components:
            print("Performing " + x + " test")

        GL.logout(self)

        # Close the browser

        # self.driver.quit()

    def genallureport(self):
        print("")

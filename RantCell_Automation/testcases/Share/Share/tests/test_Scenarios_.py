import pytest

from utilities.businessFunction.Login import LoginPage

from TestCases.Ping_Test import pingtest
from TestCases.Speed_Test_DL import speedtest_DL

class Test_do():

    def read_excel_data(filepath, Excel):
        obj = Excel
        data_extract = obj.extract_data_from_eachSheet_into_dataFrame(filepath)

        rows = []
        for data in data_extract:
            row_dict = obj.get_row_by_classifier(filepath, data["Campaigns to test"], data)
            rows.append(row_dict)
        return rows

    @pytest.mark.parametrize("test_case_", read_excel_data("../Test_data/Automation_FrameWork_Summary.xlsx"))
    def test_login(self, driver , test_case_, logger):
        try:
            username = test_case_[0]["Username"]
            password = test_case_[0]["Password"]
            driver.get(test_case_[0]["URL"])
            driver.implicitly_wait(10)
            driver.maximize_window()
            LoginPage(driver, username, password)
            txt = str(test_case_["Types of Test"])
            individual_testcase = txt.split("+")


            for testCase in individual_testcase:
                if testCase == "Ping Test" or testCase == "Ping":
                    pingtest(driver, logger, test_case_[0])

                elif testCase == "Speed Test_DL" or testCase == "Speed" or testCase == "Speed Test-DL":
                    speedtest_DL(driver, logger, test_case_)

        except AssertionError as error:
            logger.error(error)
            assert False

        except Exception as error:
            logger.error(error)
            assert False
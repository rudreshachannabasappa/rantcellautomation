import ansi2html as ansi2html
from selenium import webdriver
import pytest

driver = None

@pytest.fixture(scope="function")
def driver():
    global driver
    driver = webdriver.Chrome("../drivers/chromedriver.exe")
    yield driver
    driver.quit()
    return driver

####################################################################################################

import logging
import pytest
import os

# Define custom color codes
color_codes = {
    'DEBUG': '\033[48;5;236m\033[36m',
    'INFO': '\033[2;82m',
    'WARNING': '\033[48;5;236m\033[38;5;82m',
    'ERROR': '\033[48;5;236m\033[91m',
    'CRITICAL': '\033[48;5;236m\033[93m'
}


# Create a custom formatter that includes color codes
class ColorFormatter(logging.Formatter):
    def format(self, record):
        levelname = record.levelname
        message = record.msg
        if levelname in color_codes:
            message = color_codes[levelname] + message + '\033[0m'
        record.msg = message
        return super(ColorFormatter, self).format(record)


@pytest.fixture(scope='session')
def logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.DEBUG)

    # Define a file handler that writes logs to an HTML file
    file_handler = logging.FileHandler(os.path.join(os.path.dirname(__file__), 'logs.html'))
    file_handler.setLevel(logging.DEBUG)

    # Set the formatter for the file handler to a custom formatter that includes color codes
    formatter = ColorFormatter('%(asctime)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the file handler to the logger
    logger.addHandler(file_handler)

    # Remove the handler after the test session is complete
    yield logger
    logger.removeHandler(file_handler)

#Src
#https://rahulshettyacademy.com/blog/index.php/2021/06/06/how-to-generate-html-reports-in-pytest-framework/#:~:text=To%20generate%20HTML%20reports%20with%20the%20Pytest%20framework,skipped%2C%20one%20test%20case%20xpassed%20and%20one%20warning.
# import pytest
#
# # declare runtime variable browser_name and storing it
# def pytest_addoption(parser):
#
#     parser.addoption(
#         "--browser_name", action="store", default="chrome"
#     )
#
# # fixture method
# @pytest.fixture()
# def setup(request):
#
#     browser_name = request.config.getoption("browser_name")
#
#     if browser_name == "chrome":
#          print("Browser value passed from command line: " + browser_name)
#     elif browser_name == "firefox":
#          print("Browser value passed from command line: " + browser_name)
#     yield
#
#     print("Postcondition")
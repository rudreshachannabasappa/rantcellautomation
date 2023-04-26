import time

import pytest
from selenium import webdriver

driver = None


@pytest.fixture(scope='function')
def setup():
    global driver
    driver = webdriver.Chrome()
    #return driver
    yield driver
    # time.sleep(3)
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    """
    Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
    :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        report.when
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = "../reports/" + report.nodeid.replace("::", "_") + ".png"
            report_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % report_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    print(name)
    driver.get_screenshot_as_file(name)



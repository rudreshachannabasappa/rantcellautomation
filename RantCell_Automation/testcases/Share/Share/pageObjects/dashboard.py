from selenium.webdriver.common.by import By

class DashboardPageObjects:
    #Dashboard_Keywords
    HOMEPAGE_DASHBOARD_KEYWORD_TEXT  = (By.ID, 'refreshDashboard')
    MAP_AREA                         = (By.CLASS_NAME, "map-overlay")
    LIST_OF_CAMPAIGN_CHECKBOX        = (By.XPATH, '//input[@type="checkbox"][@id="deSelectAll"]')

    # Map-Page_Keywords
    MAP_CAMPAIGN_DROPDOWN_BTN = '(//*[@id="mainContent"]//a[@role="button"])[position()=1]'
    EXPORT_DROPDOWN_BUTTON    = (By.ID, 'exportselectionBox')
    MAP_TEXT                  = (By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Map")]]')

    #{Keywords are texts}
    MAP_KEYWORD_ONMAP         = (By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Map")]]')
    SATELLITE_KEYWORD_ONMAP   = (By.XPATH, '//div[@class="gm-style-mtc"]/button[text()[contains(.,"Satellite")]]')
    LATENCY_KEYWORD_INMAPVIEW = (By.XPATH, "//th[text()[contains(.,'Latency')]]")
    OPCOPM_KEYWORD_INMAPVIEW  = (By.XPATH, '//h6[@class="box-title hidden-xs"][text()[contains(.,"Operator Comparison")]]')
    ERROR_INMAPVIEW           = (By.XPATH, '//h3[text()[contains(.,"No test data found. Please try different date and time range.")]]')

    BLOB_ONMAP = (By.XPATH, '//div[@role="button"]/img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]')
    # Blob_OnMap = '//img[@src="https://maps.gstatic.com/mapfiles/transparent.png"]'

    TEST_DATA_TABLE_ONHOVER_OVER_MAPBLOB = (By.XPATH, '//div[@class ="info-window ng-scope"]')
    TEST_DATA_FROM_MAP                   = (By.XPATH, '//div[@class ="info-window ng-scope"]')
    # Ping_Test_data_from_Map = '//*[@id="gmaps-marker"]/div/div/div[2]/div[2]/div/div[4]/div/div/div/div[1]'

    MAP_BLOBDATA_KEYCOLUMN   = (By.XPATH, '//td[@class="option-name ng-binding"]')
    MAP_BLOBDATA_VALUECOLUMN = (By.XPATH, '//td[@class="option-value ng-binding"]')

    TEST_DATA_FROM_TABLE_MAPVIEW = (By.XPATH, '//table[@class="table-condensed table-bordered table-hover table-striped ng-scope"]')

    GRAPH_TOOLTIP = (By.XPATH, '//*[@id="chartContainer"]/div/div[@class="canvasjs-chart-tooltip"]')
class pageObjects:

    Username                      = "email"
    Password                      = "password"
    LOG_IN_BTN_ID                 = "loginbutton"
    LOGIN_FAILURE_MESSAGE_XPATH_1 = "//div[contains(text(),'Please Fill the Details for login')]"
    LOGIN_FAILURE_MESSAGE_XPATH_2 = "//div[contains(text(),'Username and password combination is wrong!')]"
    LOGIN_FAILURE_MESSAGE_1       = "Please Fill the Details for login"
    LOGIN_FAILURE_MESSAGE_2       = "Username and password combination is wrong!"

    LOGOUT_DROPDOWN               ='//a[@class="dropdown-toggle"]/span/i[2]'
    LOGOUT_DROPDOWN_ARROW         = '(//i[@class="caret"])[position()=1]'
    LOGOUT                        = '//li[@ng-click="onLogout($event)"]'
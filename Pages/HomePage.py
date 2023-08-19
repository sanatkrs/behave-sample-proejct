import time


class Homepage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        time.sleep(3)
        self.driver.find_element("xpath", "//input[@name='username']").send_keys(username)


    def enter_password(self, password):
        self.driver.find_element("xpath", "//input[@name='password']").send_keys(password)

from framework.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self, driver, locator_loader):
        super().__init__(driver, locator_loader, page_name="LoginPage")

    def login(self, username, password):
        self.input("username", username)
        self.input("password", password)
        self.click("submit")

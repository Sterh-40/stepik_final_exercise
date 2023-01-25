from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(By.XPATH, "//a[@id='login_link']").click()

    # def should_be_login_link(self):
    #     self.browser.find_element(By.XPATH, "//a[@id='login_link_invalid']")
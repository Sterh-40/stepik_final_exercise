from selenium.webdriver.common.by import By

from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        self.browser.find_element(*MainPageLocators.LOGIN_LINK).click()
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK)

    # def should_be_login_link(self):
    #     assert self.is_element_present(By.XPATH, "//a[@id='login_link_invalid']"), "Login link is not presented"

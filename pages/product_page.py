import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def add_to_cart_from_product_page(self):
        self.add_to_cart()
        self.get_alert_text()
        self.enter_code_in_prompt_window(self.solve_quiz_and_get_code(self.get_alert_text()))
        # self.println()

    def add_to_cart(self):
        self.browser.find_element(*ProductPageLocators.CART_LINK).click()

    def get_alert_text(self):
        """Get value 'x' from alert text"""
        alert = self.browser.switch_to.alert.text.split()[:3]
        return alert[2]

    def enter_code_in_prompt_window(self, code):
        self.browser.switch_to.alert.send_keys(f'{code}')
        self.browser.switch_to.alert.accept()

    def println(self):
        self.browser.implicitly_wait(10)
        ttt = self.browser.find_element(*ProductPageLocators.BOOK_NAME_1_LINK)
        # print(ttt)

    # def assertions(self):

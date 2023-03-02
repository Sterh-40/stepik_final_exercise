from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

import math


class BasePage():
    def __init__(self, browser, url, timeout=5):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, where):
        try:
            self.browser.find_element(how, where)
            return True
        except:
            NoSuchElementException
            return False

    def solve_quiz_and_get_code(self, x):
        code = str(math.log(abs(12 * math.sin(int(x)))))
        print('\ncode = ' f'{code}')
        return code

    def wait_for_alert(self, time=10):
        try:
            second_alert = WebDriverWait(self.browser, time).until(EC.alert_is_present())
        except TimeoutException:
            print("No second alert on screen")
        return second_alert
from selenium.common import NoSuchElementException
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

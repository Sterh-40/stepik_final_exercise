from selenium.common import NoSuchElementException


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

    def get_current_url(self):
        ''' return the url on your current session '''
        base_url = self.browser.current_url
        return base_url

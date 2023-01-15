import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='gb-en',
                     help="Choose language from the next list:"
                          "ar, ca, cs, da, de, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption('--language')
    print("\nStart browser test..")
    browser = webdriver.Chrome()
    # language = lang[f'{lang_key}']
    url = f"http://selenium1py.pythonanywhere.com/{f'{language}'}/"
    browser.get(url)
    #
    # if language == "lang":
    #
    # else:
    #   raise pytest.UsageError("-- language should be selected from next list:"
    #                           "ar, ca, cs, da, de, en-gb, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")
    yield browser
    print("\nQuit browser..")
    time.sleep(3)
    browser.quit()

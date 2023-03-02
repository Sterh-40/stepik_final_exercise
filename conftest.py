import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en-gb',
                     help="Choose language from the next list:"
                          "ar, ca, cs, da, de, el, es, fi, fr, it, ko, nl, pl, pt, pt-br, ro, ru, sk, uk, zh-cn")


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()

    print("\nStart browser test..")
    yield browser
    print("\nQuit browser..")
    # time.sleep(100)
    browser.quit()


@pytest.fixture(scope="function")
def url(request):
    lang = request.config.getoption('--language')
    return lang

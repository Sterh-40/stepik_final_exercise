from pages.login_page import LoginPage
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, url):
    url = f"http://selenium1py.pythonanywhere.com/{f'{url}'}/"
    page = MainPage(browser, url) # инициализация Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                   # открываем страницу
    page.go_to_login_page()       # выполняем метод страницы — переходим на страницу логина


# def test_guest_should_see_login_link(browser, url):
#     url = f"http://selenium1py.pythonanywhere.com/{f'{url}'}/"
#     page = MainPage(browser, url)
#     page.open()
#     page.should_be_login_link()

def test_should_be_login_url(browser, url):
    url = f"http://selenium1py.pythonanywhere.com/{f'{url}'}/"
    page = LoginPage(browser, url)
    page.open()
    page.should_be_login_page()
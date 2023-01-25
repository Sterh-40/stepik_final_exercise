from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser, url):
    url = f"http://selenium1py.pythonanywhere.com/{f'{url}'}/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()
    # page.should_be_login_link()

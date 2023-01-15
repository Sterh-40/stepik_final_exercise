from selenium.webdriver.common.by import By


def test_guest_can_go_to_login_page(browser):
    browser.find_element(By.XPATH, "//a[@id='login_link']").click()

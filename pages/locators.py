from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.XPATH, "//a[@id='login_link']")


class LoginPageLocators():
    LOGIN_URL = (By.XPATH, "//a[@id='login_link']")
    LOGIN_FORM = (By.XPATH, "//form[@id='login_form']")
    REGISTER_FORM = (By.XPATH, "//form[@id='register_form']")


class ProductPageLocators():
    CART_LINK = (By.XPATH, "//button[@class='btn btn-lg btn-primary btn-add-to-basket']")

    BOOK_NAME_1_LINK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/h1")
    BOOK_NAME_2_LINK = (By.XPATH, "//*[@id='messages']/div[1]/div/strong")

    BOOK_PRICE_1_LINK = (By.XPATH, "//*[@id='content_inner']/article/div[1]/div[2]/p[1]")
    BOOK_PRICE_2_LINK = (By.XPATH, "//*[@id='messages']/div[3]/div/p[1]/strong")

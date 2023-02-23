from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser, url):
    url = f"http://selenium1py.pythonanywhere.com/{f'{url}'}/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_cart_from_product_page()
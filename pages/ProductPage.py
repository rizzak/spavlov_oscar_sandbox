from pages.BasePage import BasePage


class ProductPage(BasePage):
    ALERT = '//div[@class="alertinner "]'
    MAIN_INFO = '//div[contains(@class, "product_main")]'
    PRICE = '//div[contains(@class, "product_main")]/p[@class="price_color"]'
    ADD_TO_BASKET = '//*[@id="add_to_basket_form"]'

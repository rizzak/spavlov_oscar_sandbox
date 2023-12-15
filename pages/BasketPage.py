from pages.BasePage import BasePage


class BasketPage(BasePage):
    TOTAL_PRICE = '//*[contains(@class, "total")]/h3[@class="price_color"]'
    PRODUCT_LINKS = '//*[@class="basket-items"]//img[@class="thumbnail"]/..'
    PRODUCT_PRICES = '//*[@class="basket-items"]//p[contains(@class, "price_color")]'  # Первый цена, второй всего
    CHECKOUT_BTN = '//a[contains(@href, "checkout")]'

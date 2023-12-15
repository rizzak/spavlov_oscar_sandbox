from pages.BasePage import BasePage


class CataloguePage(BasePage):
    AVAILABLE_PRODUCTS_TITLE = '//article//*[contains(@class, "instock")]/../../h3'
    AVAILABLE_PRODUCTS_PRICE = ('//div[@class="product_price"]//*[contains(@class, "instock")]/../p['
                                '@class="price_color"]')
    AVAILABLE_PRODUCTS_ADD_BASKET_BTN = '//div[@class="product_price"]//*[contains(@class, "instock")]/../form'

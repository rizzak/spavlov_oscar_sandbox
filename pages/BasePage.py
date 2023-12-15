class BasePage:
    """
    Селекторы встречающиеся на многих страницах
    """
    LOGO = '//div[contains(@class, "h1")]/a[text()="Oscar"]'
    BASKET_BLOCK = '//div[contains(@class, "basket-mini")]'
    BASKET_BTN = '//div[contains(@class, "basket-mini")]/span/a[@href="/ru/basket/"]'

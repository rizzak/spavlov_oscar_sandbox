import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from EnvironmentConfig import ENV
from pages.BasePage import BasePage
from pages.BasketPage import BasketPage
from pages.CataloguePage import CataloguePage
from pages.CheckoutPage import CheckoutPage
from pages.ProductPage import ProductPage


@allure.id("1")
@allure.story("Покупка товаров")
@allure.feature("Добавление товаров в корзину")
@allure.title("Добавление товаров в корзину")
def test_add_products_to_basket_unauthorized(browser):
    with allure.step(f'Открываем страницу "{ENV.URL}"'):
        browser.get(ENV.URL)
    items = {1: {}, 2: {}}
    with (allure.step('Добавляем первый доступный товар из каталога в корзину, запоминая id и цену')):
        items[1].update({'id': browser.find_elements(by=By.XPATH,
                    value=CataloguePage.AVAILABLE_PRODUCTS_ADD_BASKET_BTN)[0].get_attribute('action').split('/')[-2]})
        items[1].update({'price': browser.find_elements(by=By.XPATH,
                    value=CataloguePage.AVAILABLE_PRODUCTS_PRICE)[0].text.split('&')[0].split(' ')[0]})
        browser.find_elements(by=By.XPATH, value=CataloguePage.AVAILABLE_PRODUCTS_ADD_BASKET_BTN)[0].click()
    with allure.step('Переходим на карточку второго доступного товара из каталога в корзину'):
        browser.find_elements(By.XPATH, CataloguePage.AVAILABLE_PRODUCTS_TITLE)[1].click()
    with (allure.step('Добавляем товар из карточки товара в корзину, запоминая id и цену')):
        WebDriverWait(browser, 30
                      ).until(ec.presence_of_element_located((By.XPATH, ProductPage.ADD_TO_BASKET))).click()
        items[2].update(
            {'id': browser.current_url.split('_')[-1].split('/')[0]})
        items[2].update({'price': browser.find_element(by=By.XPATH, value=ProductPage.PRICE).text.split(' ')[0]})
    with allure.step('Кликаем по кнопке "Посмотреть корзину"'):
        browser.find_element(By.XPATH, BasePage.BASKET_BTN).click()
    with allure.step('Проверяем что в корзине присутствуют оба товара и цена соответствует'):
        assert browser.find_elements(
            By.XPATH, BasketPage.PRODUCT_LINKS)[1].get_attribute('href').split('_')[-1].split('/')[0] == items[2]['id']
        assert browser.find_elements(
            By.XPATH, BasketPage.PRODUCT_LINKS)[0].get_attribute('href').split('_')[-1].split('/')[0] == items[1]['id']
        price_1_in_basket = browser.find_elements(By.XPATH, BasketPage.PRODUCT_PRICES)[1].text.split(' ')[0]
        price_2_in_basket = browser.find_elements(By.XPATH, BasketPage.PRODUCT_PRICES)[3].text.split(' ')[0]
        assert price_1_in_basket == items[1]['price']
        assert price_2_in_basket == items[2]['price']
    with allure.step('Проверяем что в сумма в корзине считается корректно'):
        total_basket_price = float(browser.find_element(By.XPATH,
                                                        BasketPage.TOTAL_PRICE).text.split(' ')[0].replace(',', '.'))
        assert total_basket_price == float(price_1_in_basket.replace(',', '.')) + float(
            price_2_in_basket.replace(',', '.'))
    with allure.step('Кликаем по кнопке "Перейти к оформлению"'):
        browser.find_element(By.XPATH, BasketPage.CHECKOUT_BTN).click()
    with allure.step('Проверяем что выскакивает окно с предложением зарегистрироваться'):
        assert browser.find_element(By.XPATH, CheckoutPage.EMAIL_INPUT).is_displayed()
    with allure.step('Кликаем по лого'):
        browser.find_element(By.XPATH, BasePage.LOGO).click()
    with allure.step('Проверяем что отображается кнопка корзины с корректной суммой'):
        assert browser.find_element(By.XPATH, BasePage.BASKET_BTN).is_displayed()
        assert total_basket_price == float(browser.find_element(By.XPATH, BasePage.BASKET_BLOCK).text.split(":")[1].
                                           split("\n")[0].split(' ')[1].replace(',', '.'))

""" Фикстуры для тестов """
import pytest
from selenium import webdriver

from EnvironmentConfig import ENV


@pytest.fixture
def browser():
    """ Запуск браузера для UI тестов """
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')

    driver = webdriver.Remote(
        command_executor=f'http://{ENV.SELENIUM}/wd/hub',
        options=options
    )
    driver.set_window_size(1920, 1080)
    yield driver
    driver.close()
    driver.quit()

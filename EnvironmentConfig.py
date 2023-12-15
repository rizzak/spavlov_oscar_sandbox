import os


class EnvironmentConfig(object):
    """ Обработка переменных окружения """
    URL = os.environ.get('URL', default='https://selenium1py.pythonanywhere.com/ru/catalogue/')
    SELENIUM = os.environ.get('SELENIUM', default='localhost:4444')


ENV = EnvironmentConfig()

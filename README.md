### Запуск тестов
`pytest`

### Посмотреть Allure отчет
`allure serve allure_report`

### Запуск селениума в докере:
`docker run -d -p 4444:4444 -e VNC_NO_PASSWORD=1 --name selenium selenium/standalone-chrome`

Будет доступен локально по адресу http://localhost:4444/ui#/sessions

### После внесения правок, проверь линтером
`ruff .`

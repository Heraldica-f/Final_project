# Final_project — Автоматизация тестирования Кинопоиска

## Описание проекта
Проект предназначен для автоматизации:
- UI-тестов поиска на сайте Кинопоиск
- API-тестов поиска фильмов, персон и коллекций

UI-тесты покрывают функциональный чек-лист. 
API-тесты проверяют бизнес-логику и корректность данных.
UI-тесты помечены как xfail, так как сайт Kinopoisk использует антибот-защиту,
что приводит к нестабильному поведению при автоматизированном запуске.
Тесты включены в автозапуск и выполняются системно, однако их падение ожидаемо
и зафиксировано в тестовой документации
Проект создан в рамках финальной работы по автоматизации тестирования.

## Используемый стек
- Python 3.14
- pytest
- selenium
- undetected-chromedriver
- requests
- python-dotenv
- allure-pytest

## Структура проекта
Final_project/
├── API/
│   └── KinopoiskAPI.py
├── UI/
│   └── KinopoiskUI.py
├── config/
│   └── config.py
├── tests/
│   ├── conftest.py
│   ├── test_api.py
│   └── test_ui.py
├── requirements.txt
├── pytest.ini
├── README.md

### Шаги
1. Склонировать проект 'git clone https://github.com/Heraldica-f/Final_project.git'
2. Установить зависимости 'pip install -r requirements.txt'
3. Создать файл '.env' в корне проекта
4. Для запуска API-тестов указать в файле '.env' переменную: Kinopoisk_token, где значение Kinopoisk_token - это токен/ключ полученный через Telegram-бот
   Пример:(Переменные вписывать без пробелов до и после '=', а также значение переменных не брать в кавычки)
   Kinopoisk_token=ваш токен/ключ
5. Перейти на сайт для получения токена и нажать на кнопку "Получить токен", а далее следовать по процедуре [Получить токен здесь](https://poiskkino.dev/)
6. Убедиться, что Google Chrome установлен на компьютере
7. Закрыть ВСЕ окна браузера Google Chrome
7. Создать директорию для хранения профиля браузера, например:'C:\selenium_profiles\kinopoisk'
8. Указать путь к профилю в файле config/config.py в значении переменной Chrome_Profile_Path
9. Нажать Win + R и вставить 'chrome.exe --user-data-dir="C:\selenium_profiles\kinopoisk"'
10. Перейти на [КиноПоиск](https://www.kinopoisk.ru/)
11. Авторизоваться, пройти CAPCHA, закрыть окно браузера и повторить действия с 9 по 11 шаг для проверки сохраненного авторизованного профиля и отсутствии повторной проверки CAPCHA.
12. Запустить все тесты 'python -m pytest tests'
   Запустить отдельно api-тесты 'python -m pytest tests/test_api.py'
   Запустить отдельно ui-тесты 'python -m pytest tests/test_ui.py'
13. Allure-отчёт : 'python -m pytest tests --alluredir=allure-results
                   allure serve allure-results'

### Полезные ссылки
- [Сылка на получение токена](https://poiskkino.dev/)
- [Ссылка на документацию по проекту](https://ohayo.yonote.ru/share/e5b97c58-8077-493a-990e-8dc3c18f3c4a)
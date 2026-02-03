import pytest
import allure
import undetected_chromedriver as uc
from UI.KinopoiskUI import KinopoiskUI
from config.config import Chrome_Profile_Path

@pytest.fixture(scope="session")
@allure.title("Настройка и создание драйвера Chrome (Undetected)")
def chrome_driver():
    """
    Фикстура для создания драйвера Chrome с с обходом защиты (Anti-Bot)
    
    :yield: Настроенный экземпляр WebDriver
    :rtype: WebDriver 
    """
    options = uc.ChromeOptions()

    options.add_argument("--start-maximized")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    options.add_argument(f"--user-data-dir={Chrome_Profile_Path}")

    driver = uc.Chrome(options=options, version_main=144)

    yield driver

    driver.quit()

@pytest.fixture
@allure.title("Создание экземпляра KinopoiskUI")
def kinopoisk(chrome_driver):
    """
    Фикстура для создания экземпляра Page Object
    
    :param chrome_driver: Настроенный драйвер Chrome
    :type chrome_driver: WebDriver
    :return: Экземпляр KinopoiskUI
    :rtype: KinopoiskUI
    """
    return KinopoiskUI(chrome_driver)

@pytest.fixture
@allure.title("Подготовка KinopoiskUI с открытым сайтом")
def kinopoisk_on_site(kinopoisk):
    """
    Открывает страницу сайта Кинопоиск
    
    :param kinopoisk: Экземпляр KinopoiskUI
    :type kinopoisk: KinopoiskUI
    :return: KinopoiskUI с открытым сайтом
    :rtype: KinopoiskUI
    """
    kinopoisk.open_window()
    
    return kinopoisk
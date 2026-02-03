import allure

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from config.config import UI_base_url


class KinopoiskUI:
    """
    Page Object UI для сайта Кинопоиск
    """
    url = UI_base_url
    Search_Field = (By.CSS_SELECTOR, 'input[name="kp_query"]')
    Search_Results = (By.CSS_SELECTOR, '[data-tid="SearchList"]')
    No_Results_Message = (By.XPATH, '//*[contains(text(),"ничего не найдено")]')
    

    def __init__(self, driver) -> None:
        """
        Инициализация Page Object
        
        :param driver: WebDriver экземпляр
        :type driver: WebDriver
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Перейти на главную страницу")
    def open_window(self) -> None:
        """
        Подгружает страницу КиноПоиска
        """
        self.driver.get(self.url)

    @allure.step("Ввести текст '{text}' в поиск и отправить запрос")
    def text_input(self, text: str) -> None:
        """
        Находит строку поиска, очищает ее, вводит значение параметра text и отправляет запрос 
        
        :param text: значение для ввода в строку поиска
        :type text: str
        """
        search_field  = self.wait.until(
            EC.element_to_be_clickable(self.Search_Field))
        
        search_field.clear()
        search_field.send_keys(text)
        search_field.send_keys(Keys.RETURN)

    @allure.step("Проверить наличие результатов поиска")
    def presence_search_results(self) -> bool:
        """
        Проверяет наличие результатов поиска на странице
        
        :return: True если есть результаты, в противном случае False
        :rtype: bool
        """
        try:
            self.wait.until(
                EC.presence_of_element_located(self.Search_Results)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Проверить наличие сообщения 'К сожалению, по вашему запросу ничего не найдено...'")
    def no_results_presence(self) -> bool:
        """
        Проверяет наличие сообщения об отсутствии результатов поиска
        
        :return: True если есть сообщение, иначе False
        :rtype: bool
        """
        try:
            self.wait.until(
                EC.presence_of_element_located(self.No_Results_Message)
            )
            return True
        except TimeoutException:
            return False
    
    @allure.step("Получить текст сообщения об отсутствии результатов поиска")
    def get_no_results_message(self) -> str:
        """
        Возвращает текст сообщения 'К сожалению, по вашему запросу ничего не найдено...'
        """
        try:
            message = self.wait.until(
                EC.presence_of_element_located(self.No_Results_Message)
            )
            return message.text.lower()
        except TimeoutException:
            return ""
        
    @allure.step("Проверить, что при отправке запроса url не изменился")
    def is_on_main_page(self) -> bool:
        """
        Проверяет отсутсвие изменения url после отправки запроса
        
        :return: True если url не изменился, в противном случае False
        :rtype: bool
        """
        return self.driver.current_url.rstrip("/") == self.url.rstrip("/")


        

        

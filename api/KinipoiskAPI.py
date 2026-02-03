import requests
import allure
from typing import Any

class KinopoiskAPI:
    """
    Page Object API для сайта Кинопоиск
    """

    def __init__(self, base_url: str, token: str) -> None:
        """
        Инициализация Page Object
        
        :param base_url: Базовый url 
        :type base_url: str
        :param token: Токен авторизации
        :type token: str
        """
        self.base_url: str = base_url
        self.token: str = token

    @allure.step("Поиск фильма по названию")
    def search_movie(self, title: str) -> requests.Response:
        """
        Поиск фильма по названию
        
        :param title: Название фильма
        :type title: str
        :return: Описание
        :rtype: Response
        """
        headers: dict[str, str] = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params: dict[str, Any] = {
            'page': 1,
            'limit': 10,
            'query': title
        }

        resp = requests.get(f"{self.base_url}/movie/search", headers=headers, params=params)
        return resp
    
    @allure.step("Поиск работника киноиндустрии по имени")
    def search_worker(self, name: str) -> requests.Response:
        """
        Поиск работника киноиндустрии по имени
        
        :param name: Имя работника киноиндустрии
        :type name: str
        :return: Описание
        :rtype: Response
        """
        headers: dict[str, str] = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params: dict[str, Any] = {
            'page': 1,
            'limit': 10,
            'query': name
        }

        resp = requests.get(f"{self.base_url}/person/search", headers=headers, params=params)
        return resp
    
    @allure.step("Поиск коллекций фильмов ао категории")
    def searching_collections(self, category: str) -> requests.Response:
        """
        Поиск коллекций фильмов по категории
        
        :param category: Категория коллекции фильмов
        :type category: str
        :return: Описание
        :rtype: Response
        """
        headers: dict[str, str] = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params: dict[str, Any] = {
            'page': 1,
            'limit': 10,
            'category': category
        }
        resp = requests.get(f"{self.base_url}/list", headers=headers, params=params)
        return resp
    
    @allure.step("Поиск коллекции фильмов без указания парметров поиска")
    def emty_searching_collections(self, category: str) -> requests.Response:
        """
        Поиск коллекции фильмов без указания парметров поиска
        
        :param category: Категория коллекции фильмов
        :type category: str
        :return: 
        :rtype: Response
        """
        headers: dict[str, str] = {
            "accept": "application/json",
            "X-API-KEY": self.token
        }

        params: dict[str, Any] = {
            'page': '',
            'limit': '',
            'category': category
        }

        resp = requests.get(f"{self.base_url}/list", headers=headers, params=params)
        return resp
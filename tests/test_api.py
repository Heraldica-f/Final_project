import allure

from API.KinipoiskAPI import KinopoiskAPI
from config.config import API_base_url
import os
from dotenv import load_dotenv

load_dotenv()

@allure.epic("Kinopoisk API")
@allure.feature("Поиск")
class TestKinopoiskAPI:

    base_url = API_base_url
    token = os.getenv("Kinopoisk_token")

    api = KinopoiskAPI(base_url, token)

    @allure.id("KinopoiskAPI1")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Поиск фильма по названию")
    @allure.description("Проверка поиска фильма по названию")
    def test_searching_film_by_name(self):
        resp = self.api.search_movie('Бригада')

        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно больше 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) > 0

        with allure.step("Проверить, что переданный параметр соответсвует параметру результата поиска"):
            first_film = resp_data["docs"][0]
            assert first_film["name"] == 'Бригада'

    @allure.id("KinopoiskAPI2")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Поиск работников киноиндустрии по имени")
    @allure.description("Проверка поиска работников киноиндустрии по имени и фамилии")
    def test_searching_film_idustry_worker(self):
        resp = self.api.search_worker('Сергей Безруков')

        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно больше 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) > 0

        with allure.step("Проверить, что переданный параметр соответсвует параметру результата поиска"):
            first_person = resp_data["docs"][0]
            assert first_person["name"] == 'Сергей Безруков'

    @allure.id("KinopoiskAPI3")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Получение коллекций по категории")
    @allure.description("Проверка получения коллекций фильмов по заданной категории")
    def test_searching_film_collections(self):
        category_list = {
            '0': 'Фильмы',
            '1': 'Онлайн-кинотеатр',
            '2': 'Премии',
            '3': 'Сборы',
            '4': 'Сериалы'
        }
        resp = self.api.searching_collections(category_list['0'])
        
        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно больше 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) > 0

        with allure.step("Проверить, что переданный параметр соответсвует параметру результата поиска"):
            first_coll = resp_data["docs"][0]
            assert first_coll["category"] == category_list['0']

    @allure.id("KinopoiskAPI4")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Валидация параметров запроса")
    @allure.description("Проверка корректной обработки запроса без обязательных параметров")
    def test_searching_collections_without_parameters(self):
        resp = self.api.emty_searching_collections('')
        
        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 400

        with allure.step("Проверить, что результатом поиска является ошибка и сверить текст ошибки"):
            resp_data = resp.json()
            assert resp_data["error"] == "Bad Request"

    @allure.id("KinopoiskAPI5")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Валидация параметров запроса")
    @allure.description("Проверка обработки запроса с некорректным значением параметра category")
    def test_searching_collections_with_uncorrect_parameter(self):
        resp = self.api.searching_collections('Комедии')
            
        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 400

        with allure.step("Проверить, что результатом поиска является ошибка и сверить текст ошибки"):
            resp_data= resp.json()
            assert resp_data["error"] == "Bad Request"

    @allure.id("KinopoiskAPI6")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Поиск фильма без параметров")
    @allure.description("Проверка поведения API при поиске фильма без указания названия")
    def test_searching_film_without_name(self):
        resp =self.api.search_movie('')

        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно больше 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) > 0

    @allure.id("KinopoiskAPI7")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Поиск работников киноиндустрии без параметров")
    @allure.description("Проверка поведения API при поиске персоны без указания имени")
    def test_searching_an_actor_without_name(self):
        resp = self.api.search_worker('')
        
        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно больше 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) > 0

    @allure.id("KinopoiskAPI8")
    @allure.severity(allure.severity_level.MINOR)
    @allure.story("Поиск работников киноиндустрии с несуществующими данными")
    @allure.description("Проверка поиска персоны с несуществующим именем")
    def test_searching_an_actor_with_defunct_name(self):
        resp = self.api.search_worker('Элмордвик')

        with allure.step("Проверить status code ответа"):
            assert resp.status_code == 200

        with allure.step("Проверить наличие тела ответа и что оно равно 0"):
            resp_data = resp.json()
            assert "docs" in resp_data
            assert len(resp_data["docs"]) == 0
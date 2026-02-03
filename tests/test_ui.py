import allure
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.xfail(reason="Kinopoisk активно блокирует автотесты")
@allure.epic("UI Тесты")
@allure.feature("Поиск")
@allure.story("Обработка пользовательского ввода")
class TestSearchField:
    """
    Тесты функциональности поиска на сайте Кинопоиск
    """
    @allure.id("Kinopoisk1")
    @allure.title("Текст кириллицей")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка, что поиск корректно обрабатывает ввод на кириллице и возвращает результаты")
    def text_in_cyrillic_test(self, kinopoisk_on_site):
        """
        Проверка поиска по тексту кириллицей
        
        Ожидаемый результат:
        - Найдены результаты поиска
        - В результатах есть искомый текст
        """
        search_text = 'Интерстеллар'
        kinopoisk_on_site.text_input(search_text) 
        assert kinopoisk_on_site.presence_search_results()

    @allure.id("Kinopoisk2")
    @allure.title("Текст латиницей")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка, что поиск корректно обрабатывает ввод на латинице и возвращает результаты")
    def text_in_latin_test(self, kinopoisk_on_site):
        """
        Проверка поиска по тексту латиницей
        
        Ожидаемый результат:
        - Найдены результаты поиска
        """
        search_text = 'Interstellar'  
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()

    @allure.id("Kinopoisk3")
    @allure.title("Текст со знаками препинания")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка, что знаки препинания в поисковом запросе корректно игнорируются и не влияют на результаты поиска")
    def text_with_punctuation_marks_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста со знаками препинания
        
        Ожидаемый результат:
        - Поиск обработан корректно
        - Знаки препинания игнорируются
        """
        search_text = 'Interstellar!'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()

    @allure.id("Kinopoisk4")
    @allure.title("Текст с цифрами")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка обработки поискового запроса, содержащего текст и цифры")
    @pytest.mark.xfail(reason="Поиск с цифрами ведет себя непоследовательно")
    def text_with_nums_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста с цифрами
        
        Ожидаемый результат:
        - Найдены результаты поиска
        """
        search_text = 'Интерстеллар123'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()
        
    @allure.id("Kinopoisk5")
    @allure.title("Цифры")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка поиска по числовому запросу (например, год выпуска фильма)")
    def nums_test(self, kinopoisk_on_site):
        """
        Проверка поиска только цифрами
        
        Ожидаемый результат:
        - Найдены фильмы соответствующего года
        """
        search_text = '2020'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()

    @allure.id("Kinopoisk6")
    @allure.title("Текст со спецсимволами:@#$%^&*")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка игнорирования специальных символов в составе текстового поискового запроса")
    def text_with_special_characters_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста со специальными символами
        
        Ожидаемый результат:
        - Спецсимволы игнорируются
        - Поиск выполняется по текстовой части
        """
        search_text = 'Интерстеллар@#$'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()

    @allure.id("Kinopoisk7")
    @allure.title("Спецсимволы:@#$%^&*")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Проверка поведения поиска при вводе только специальных символов")
    @pytest.mark.xfail(reason="Поиск со спецсимволами может выявить существующие фильмы")
    def special_characters_test(self, kinopoisk_on_site):
        """
        Проверка поиска только специальными символами
        
        Ожидаемый результат:
        - Нет результатов поиска
        - Возможно сообщение 'К сожалению, по вашему запросу ничего не найдено...'
        """
        search_text = '@#$%^&*'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.no_results_presence()
    
    @allure.id("Kinopoisk8")
    @allure.title("Текст в нижнем регистре")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка регистронезависимости поиска при вводе текста в нижнем регистре")
    def lowercase_text_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста в нижнем регистре
        
        Ожидаемый результат:
        - Поиск регистронезависимый
        - Найдены результаты
        """
        search_text = 'interstellar'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()
    
    @allure.id("Kinopoisk9")
    @allure.title("Текст в верхнем регистре")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка регистронезависимости поиска при вводе текста в верхнем регистре")
    def uppercase_text_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста в верхнем регистре
        
        Ожидаемый результат:
        - Поиск регистронезависимый
        - Найдены результаты
        """
        search_text = 'INTERSTELLAR'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()
    
    @allure.id("Kinopoisk10")
    @allure.title("Текст в смешанном регистре")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка корректной обработки поискового запроса в смешанном регистре")
    def uppercase_and_lowercase_text_test(self, kinopoisk_on_site):
        """
        Проверка поиска текста в смешанном регистре
        
        Ожидаемый результат:
        - Поиск регистронезависимый
        - Найдены результаты
        """
        search_text = 'ИнТеРсТеЛлАр'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()
    
    @allure.id("Kinopoisk11")
    @allure.title("Знаки препинания")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Проверка отображения сообщения об отсутствии результатов при вводе только знаков препинания")
    def punctuation_marks_test(self, kinopoisk_on_site):
        """
        Проверка поиска только знаками препинания
        
        Ожидаемый результат:
        - Нет результатов поиска
        - Возможно сообщение 'К сожалению, по вашему запросу ничего не найдено...'
        """
        search_text = '.,!?;:—'

        kinopoisk_on_site.text_input(search_text)
        
        assert kinopoisk_on_site.no_results_presence()
        result_mesage = kinopoisk_on_site.get_no_results_message()
        with allure.step("Сверить, что текст сообщения совпадает с полученным"):
            assert 'к сожалению, по вашему запросу ничего не найдено' in result_mesage

    
    @allure.id("Kinopoisk12")
    @allure.title("Пустое поле")
    @allure.severity(allure.severity_level.CRITICAL)
    @allure.description("Проверка поведения поиска при отправке пустого запроса")
    def emty_field_test(self, kinopoisk_on_site):
        """
        Проверка поиска с пустым полем ввода
        
        Ожидаемый результат:
        - Остаемся на той же странице
        - URL не изменяется
        """
        kinopoisk_on_site.text_input('')
        assert kinopoisk_on_site.is_on_main_page()

    
    @allure.id("Kinopoisk13")
    @allure.title("Текст длинной в 30 символов")
    @allure.severity(allure.severity_level.MINOR)
    @allure.description("Проверка обработки длинного поискового запроса без ожидаемых результатов")
    @pytest.mark.xfail(reason="Длинные рандомные строки обрабатываются поиском непоследовательно")
    def text_length_30_characters_test(self, kinopoisk_on_site):
        """
        Проверка поиска длинного текста
        
        Ожидаемый результат:
        - Нет результатов поиска
        - Возможно сообщение 'К сожалению, по вашему запросу ничего не найдено...'
        """
        search_text = 'djhoihgxoidjhoihgxoidjhoihgxoi'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.no_results_presence()

    
    @allure.id("Kinopoisk14")
    @allure.title("Название фильма из нескольких слов без пробелов")
    @allure.severity(allure.severity_level.NORMAL)
    @allure.description("Проверка способности поиска корректно интерпретировать запрос без пробелов между словами")
    def title_without_spaces_test(self, kinopoisk_on_site):
        """
        Проверка поиска названия без пробелов
        
        Ожидаемый результат:
        - Поиск пытается разделить слова
        - Найдены результаты или подсказки
        """
        search_text = 'ИнтерстелларКристоферНолан'
        kinopoisk_on_site.text_input(search_text)
        assert kinopoisk_on_site.presence_search_results()
            

    
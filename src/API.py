import os
from abc import ABC
from abc import abstractmethod
import requests


class BaseApi(ABC):
    """
    Абстрактный класс для работы с API сайтов с вакансиями
    """

    @abstractmethod
    def get_vacancies(self, keyword):
        pass


class HeadHunterApi(BaseApi):
    """
    Класс для работы с API сайта HeadHunter с вакансиями
    """

    def __init__(self):
        """
        Инициализатор класса HeadHunterApi
        """
        self.url = "https://api.hh.ru/vacancies"
        self.data_response = None

    def get_vacancies(self, keyword):
        """
        Получает список вакансий с сайта HeadHunter по ключевому слову
        """
        headers = {"User-Agent": "kirillOreshchuk"}
        params = {'text': keyword,
                  "only_with_salary": True,
                  "per_page": 20
                  }
        response = requests.get(self.url, headers=headers, params=params).json()

        return response


class SuperJobApi(BaseApi):
    """
    Класс для работы с API сайта SuperJob с вакансиями
    """

    def __init__(self):
        """
        Инициализатор класса SuperJobApi
        """
        self.url = 'https://api.superjob.ru/2.0/vacancies/'
        self.data_response = None

    def get_vacancies(self, vacancy):
        """
        Получает список вакансий с сайта SuperJob по ключевому слову
        """

        secret_key = os.getenv("SECRET_KEY")

        headers = {"Host": 'api.superjob.ru',
                   "X-Api-App-Id": secret_key,
                   "Authorization": "Bearer r.000000010000001.example.access_token",
                   "Content-Type": "application/x-www-form-urlencoded"}

        params = {"keyword": vacancy,
                  'payment_defined': 1,
                  "only_with_salary": True,
                  "per_page": 20
                  }

        response = requests.get(self.url, headers=headers, params=params).json()

        return response

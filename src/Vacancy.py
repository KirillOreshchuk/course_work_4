class Vacancy:
    """
    Класс для работы с вакансиями
    """

    def __init__(self, name, url, area, salary_from, salary_to, salary_currency, responsibility):
        """
        Инициализатор класса Vacancy
        """
        self.name = name
        self.url = url
        self.area = area
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.salary_currency = salary_currency
        self.responsibility = responsibility

    def __str__(self):
        """
        возвращает строковое представление экземпляра класса Vacancy
        :return:
        """
        return (f"Вакансия: {self.name}\n"
                f"Ссылка {self.url}\n"
                f"Местоположение: {self.area}\n"
                f"Зарплата от {self.salary_from} до {self.salary_to} {self.salary_currency}\n"
                f"Требования: {self.responsibility}\n")

    def compare(self, other):
        """
        Метод для сравнения вакансий по заработной плате
        """

        if self.salary_currency != other.salary_currency:
            return f"Вакансии нельзя сравнить, разная валюта."
        try:
            if int(self.salary_from) > int(other.salary_from) or int(self.salary_to) > int(other.salary_to):
                return (f"Вакансия '{self.name}' имеет большую зарплату чем вакансия '{other.name}'.\n"
                        f"Вакансия '{self.name}' предлагает зарплату от {self.salary_from}"
                        f" до {self.salary_to} {self.salary_currency}")

            elif int(self.salary_from) < int(other.salary_from) or int(self.salary_to) < int(other.salary_to):
                return (f"Вакансия '{other.name}' имеет зарплату больше чем вакансия '{self.name}'.\n"
                        f"Вакансия '{other.name}' предлагает зарплату от {other.salary_from}"
                        f" до {other.salary_to} {other.salary_currency}")

        except TypeError:
            print("Вакансии нельзя сравнить, некорректные данные"
                  " (отсутствует 'заработная плата от' или 'заработная плата')")
        except UnboundLocalError:
            print("Одна или обе вакансии отсутствуют в списке")


def format_data_hh(any_data):
    """
        Форматирует JSON-словарь вакансий с сайта HeadHunter в удобный вид
        """
    for vacancy in any_data["items"]:
        name = vacancy["name"]
        city = vacancy["area"]["name"]
        salary_from = vacancy["salary"]["from"]
        if salary_from is None:
            salary_from = "не указано"
        salary_to = vacancy["salary"]["to"]
        if salary_to is None:
            salary_to = "не указано"
        currency = vacancy["salary"]["currency"]
        if currency is None:
            currency = "не указано"
        url = vacancy["url"]
        responsibilities = vacancy["snippet"]["responsibility"]

        print(f"Вакансия: {name}\nГород: {city}\nЗарплата от: {salary_from} до {salary_to} {currency}.")
        print(f"Ссылка: {url}\nТребования: {responsibilities}\n")\



def format_data_sj(any_data):
    """
    Форматирует JSON-словарь вакансий с сайта SuperJob в удобный вид
    """
    for vacancy in any_data["objects"]:
        name = vacancy["profession"]
        city = vacancy["address"]
        salary_from = vacancy["payment_from"]
        if salary_from is None or salary_from == 0:
            salary_from = "не указано"
        salary_to = vacancy["payment_to"]
        if salary_to is None or salary_to == 0:
            salary_to = "не указано"
        currency = vacancy["currency"]
        if currency is None or currency == 0:
            currency = "не указано"
        url = vacancy["link"]
        responsibilities = vacancy["candidat"]

        print(f"Название: {name}\nГород: {city}\nЗарплата: от {salary_from} до {salary_to} {currency}.")
        print(f"Ссылка: {url}\nТребования: {responsibilities}\n")

from abc import ABC, abstractmethod
import json


class JsonManagerAbstract(ABC):
    """
    абстрактный класс, который обязывает реализовать методы для добавления вакансий в файл
    """

    @abstractmethod
    def add_vacancy(self, name):
        pass

    @abstractmethod
    def delete_vacancy(self, name):
        pass


class JsonManager(JsonManagerAbstract):

    def __init__(self, file):
        """
        Инициализатор класса JsonManager
        :param file:
        """
        self.file = file
        self.name = ""

    def save_file(self, file):

        with open(self.file, 'w', encoding="utf-8") as f:
            json.dump(file, f, ensure_ascii=False, indent=4)

    def add_vacancy(self, name):
        """
        Добавляет вакансии в файл
        :param name:
        :return:
        """
        self.name = name
        with open(self.file, 'w', encoding='utf-8') as file:
            json.dump(self.name, file, ensure_ascii=False, indent=4)

    def delete_vacancy(self, name):
        """
        Удаляет вакансию из файла по названию
        """
        with open(self.file, 'r', encoding='utf-8') as file:
            data = json.load(file) # открываем файл

        new_vac_list = []
        for del_vacancy in data["items"]:
            if del_vacancy["name"] == name:
                pass
            else:
                new_vac_list.append(del_vacancy)

        with open(self.file, "w", encoding="utf-8") as file:
            json.dump({"items": new_vac_list}, file, ensure_ascii=False, indent=4)


def open_json(file_name):
    """Открывает файл json"""
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
        return data

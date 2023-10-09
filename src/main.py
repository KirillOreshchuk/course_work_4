from JsonManager import JsonManager
from API import HeadHunterApi, SuperJobApi
from Vacancy import Vacancy, format_data_hh, format_data_sj
from JsonManager import open_json


def main():

    print("Привет! Сегодня будем искать подходящие вакансии. У нас есть две платформы: HeadHunter и SuperJob.")
    while True:
        try:
            platform = int(input("На какой платформе будем искать? 1 - hh.ru, 2 - sj.ru\n"))
        except ValueError:
            print("Вы ввели некорректный ответ, пожалуйста, повторите попытку")
            continue

        if platform == 1:
            print("Отлично, будем искать на HeadHunter!")
            hh_api = HeadHunterApi()

            keyword = input("Введите ключевое слово, по которому будем искать подходящие вакансии:\n")
            vacancies = hh_api.get_vacancies(keyword)

            json_hh = JsonManager("vacancies_hh.json")
            json_hh.add_vacancy(vacancies)
            data = open_json("vacancies_hh.json")

            print("Вот вакансии подходящие для вас: \n")
            format_data_hh(data)

            while True:
                try:
                    compare_input = int(input("Хотите сравнить вакансии? 1 - да, 2 - нет\n"))

                except ValueError:
                    print("Вы ввели некорректный ответ, пожалуйста, повторите попытку")
                    continue

                if compare_input == 1:

                    print("Отлично, будем сравнивать!")

                    vacancy1 = input("Введите название первой вакансии:\n")
                    vacancy2 = input("Введите название второй вакансии:\n")

                    for vacancy in data["items"]:
                        if vacancy1 == vacancy["name"]:
                            class_vacancy1 = Vacancy(vacancy1,
                                                     vacancy["url"],
                                                     vacancy["area"]["name"],
                                                     vacancy["salary"]["from"],
                                                     vacancy["salary"]["to"],
                                                     vacancy["salary"]["currency"],
                                                     vacancy["snippet"]["responsibility"]
                                                     )

                        elif vacancy2 == vacancy["name"]:
                            class_vacancy2 = Vacancy(vacancy2,
                                                     vacancy["url"],
                                                     vacancy["area"]["name"],
                                                     vacancy["salary"]["from"],
                                                     vacancy["salary"]["to"],
                                                     vacancy["salary"]["currency"],
                                                     vacancy["snippet"]["responsibility"]
                                                     )

                    try:
                        result_compare = class_vacancy1.compare(class_vacancy2)
                        print(result_compare)
                        print("Спасибо за использование приложения.")

                    except UnboundLocalError:
                        print("Одна или обе вакансии отсутствуют в списке, спасибо за использование приложения")

                elif compare_input == 2:
                    print("Сравнение отменено, спасибо за использование приложения.")
                    break
                else:
                    print("Вы ввели некорректный ответ, пожалуйста, повторите попытку.")
                    continue

                break

            break

        elif platform == 2:

            print("Отлично, будем искать на SuperJob!")
            sj_api = SuperJobApi()

            keyword = input("Введите ключевое слово, по которому будем искать подходящие вакансии:\n")
            vacancies = sj_api.get_vacancies(keyword)

            sj_json = JsonManager("vacancies_sj.json")
            sj_json.add_vacancy(vacancies)
            data = open_json("vacancies_sj.json")

            print("Вот вакансии подходящие для вас:\n")
            format_data_sj(data)

            while True:

                compare_input = int(input("Хотите сравнить вакансии? 1 - да, 2 - нет\n"))

                if compare_input == 1:

                    print("Отлично, будем сравнивать!")

                    vacancy1 = input("Введите название первой вакансии: ")
                    vacancy2 = input("Введите название второй вакансии: ")

                    for vacancy in data["objects"]:
                        if vacancy1 == vacancy["profession"]:
                            class_vacancy1 = Vacancy(vacancy1,
                                                     vacancy["link"],
                                                     vacancy["address"],
                                                     vacancy["payment_from"],
                                                     vacancy["payment_to"],
                                                     vacancy["currency"],
                                                     vacancy["candidat"])

                        elif vacancy2 == vacancy["profession"]:
                            class_vacancy2 = Vacancy(vacancy2,
                                                     vacancy["link"],
                                                     vacancy["address"],
                                                     vacancy["payment_from"],
                                                     vacancy["payment_to"],
                                                     vacancy["currency"],
                                                     vacancy["candidat"])

                    try:
                        result_compare = class_vacancy1.compare(class_vacancy2)
                        print(result_compare)
                        print("Спасибо за использование приложения.")

                    except UnboundLocalError:
                        print("Одна или обе вакансии отсутствуют в списке, спасибо за использование приложения.")

                elif compare_input == 2:
                    print("Сравнение отменено, спасибо за использование приложения.")
                    break
                else:
                    print("Вы ввели некорректный ответ, пожалуйста, повторите попытку.")
                    continue

                break

        else:
            print("Вы ввели некорректный ответ, пожалуйста, повторите попытку")
            continue

        break


main()

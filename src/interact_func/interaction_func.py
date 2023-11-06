from src.api_classes.sj_api_class import SuperJobAPI
from src.api_classes.hh_api_class import HeadHunterAPI
from src.savers.specialized_savers.json_saving import JSONSaving
from os import getenv
from json import dumps


def operator_act(operator):
    while True:
        acts = ("сорт_зп", "топ", "фильтр_зп", "фильтр_сл", "вывод", "выход")
        print("Что нужно сделать c Вакансиями?>>> ", end="")
        act = input()

        if " " in act and act.split()[0] not in acts:
            print("ошибка")
            continue

        if act == "выход":
            print("конец")
            return operator

        if act == "вывод":
            string = dumps(operator.dict, indent=2, ensure_ascii=False)
            print(string)
            continue

        if act == "сорт_зп":
            operator = operator.sort_by_salary()
            continue

        if " " not in act:
            print("ошибка")
            continue

        if act.split()[0] == "фильтр_зп":
            ran = list(map(int, act.split()[1].split("-")))
            operator.filter_by_salary_range(ran[0], ran[1])
            continue

        if act.split()[0] == "фильтр_сл":
            operator.filter_by_keyword(act.split()[1])
            continue

        if act.split()[0] == "топ":
            operator.get_top_n(int(act.split()[1]))


def platform_act():
    platforms = ("HH", "SH")
    platform = input("введите название платформы: \"HH\" или \"SJ\"")
    if platform.upper() not in platforms:
        print("нет такой платформы")

    if platform.upper() == "HH":
        platform_obj = HeadHunterAPI()
    else:
        platform_obj = SuperJobAPI(getenv("SJ_API_KEY"))

    print("Введите ключевое слово для поиска:")
    keyword = input()

    if keyword == "":
        keyword = None

    vac_list = platform_obj.get_vacancies(keyword)
    file_to_save = input("введите название файла для сохранения:\n")
    name = input("Введите название списка вакансий")

    if file_to_save == "" or ".json" != file_to_save[-5:]:
        print("Некорректный файл")
        return

    if name == "":
        name = None

    with JSONSaving(file_to_open=None, file_to_save=file_to_save, title=name) as operator:
        operator.list = vac_list
        operator_act(operator)


def file_act():
    print("Введите название файла json для открытия:")
    file_to_open = input()

    print("Введите название файла json для сохранения:")
    file_to_save = input()

    if file_to_open == "" or ".json" != file_to_open[-5:]:
        print("Некорректный файл")
        return

    if file_to_save == "" or ".json" != file_to_save[-5:]:
        print("Некорректный файл")
        return

    with JSONSaving(file_to_open, file_to_save, None) as operator:
        operator_act(operator)


def main():
    acts = ("1", "2")
    act = input("Укажите действие: новые вакансии с платформ: введите 1, вакансии из файла: введите 2")
    if act not in acts:
        print("нет такого действия")

    if act == "1":
        platform_act()

    else:
        file_act()


if __name__ == "__main__":
    main()

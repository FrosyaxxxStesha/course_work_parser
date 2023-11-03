from src.vacancy_classes.vacancy_class import Vacancy


class VacancyOperator:
    def __init__(self, title: str, list_of_vacs: list[Vacancy] | None = None) -> None:
        if list_of_vacs is None:
            list_of_vacs = []

        elif not isinstance(list_of_vacs, list):
            raise ValueError("Коллекцией хранения вакансий должен быть список")

        elif not all(map(lambda vac: isinstance(vac, Vacancy), list_of_vacs)):
            raise ValueError("В списке вакансий могут находится только экземпляры класса Vacancy")

        if not isinstance(title, str):
            raise ValueError("Название должно быть строкой")

        self.__title = title
        self.__vac_list = list_of_vacs

    @property
    def __count(self):
        return len(self.__vac_list)



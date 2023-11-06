from src.vacancy_classes.vacancy_class import Vacancy


class VacancyOperator:
    """Класс для работы с вакансиями"""
    def __init__(self, title: str, list_of_vacs: list[Vacancy] | None = None) -> None:
        """Инициализатор класса для работы с вакансиями"""
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
    def __count(self) -> int:
        """Возвращает количество вакансий"""
        return len(self.__vac_list)

    @property
    def list(self) -> list[Vacancy]:
        """Возвращает список вакансий"""
        return self.__vac_list

    @list.setter
    def list(self, vac_list: list[Vacancy]) -> None:
        """Возвращает список вакансий"""
        self.__vac_list = vac_list

    @property
    def dict(self) -> dict:
        """Возвращает словарь с атрибутами класса"""
        return {
            "title": self.__title,
            "count": self.__count,
            "list_of_vacs": list(map(lambda vac: vac.vacancy_dict, self.__vac_list))
                }

    @classmethod
    def from_dict(cls, dict_):
        """Инициализация объекта класса из словаря"""
        dict_["list_of_vacs"] = list(map(lambda vac_dict: Vacancy(**vac_dict), dict_["list_of_vacs"]))
        del dict_["count"]
        return cls(**dict_)

    @staticmethod
    def _filter_by_kw_key(vac: Vacancy, kw: str) -> bool:
        """Фильтрация по ключевому слову для одной вакансии"""
        if kw in vac.vacancy_dict["title"]:
            return True
        elif kw in vac.vacancy_dict["url"]:
            return True
        if vac.vacancy_dict["requirements"] is None:
            pass
        elif kw in vac.vacancy_dict["requirements"]:
            return True
        if vac.vacancy_dict["responsibility"] is None:
            pass
        elif kw in vac.vacancy_dict["responsibility"]:
            return True
        return False

    def filter_by_keyword(self, keyword: str) -> None:
        """Фильтрация по ключевому слову для всей вакансии"""
        self.__vac_list = list(filter(lambda vac: self._filter_by_kw_key(vac, keyword), self.__vac_list))

    def filter_by_salary_range(self, min_s: int, max_s: int) -> None:
        """Фильтр по диапазону зарплат"""
        if max_s < min_s:
            raise ValueError("Максимальная зарплата не должна быть меньше минимальной")
        self.__vac_list = list(filter(lambda vac: min_s <= vac.salary <= max_s, self.__vac_list))

    def filter_by_platform(self, pl_name: str) -> None:
        """Фильтр по платформе"""
        self.__vac_list = list(filter(lambda vac: pl_name in vac.__url, self.__vac_list))

    def sort_by_salary(self, reverse: bool = False) -> None:
        """Сортировка по зарплате"""
        self.__vac_list.sort(key=lambda vac: vac.salary, reverse=reverse)

    def get_top_n(self, n: int) -> None:
        """Фильтр топ n вакансий"""
        self.sort_by_salary(reverse=True)
        self.__vac_list = self.__vac_list[:n]

    def add_vacancy(self, vac: Vacancy) -> None:
        """Добавление вакансии"""
        self.__vac_list.append(vac)

    def del_vacancy(self, vac: Vacancy) -> None:
        """Удаление Вакансии"""
        self.__vac_list.remove(vac)

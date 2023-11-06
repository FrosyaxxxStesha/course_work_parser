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

    @property
    def list(self) -> list[Vacancy]:
        return self.__vac_list

    @list.setter
    def list(self, vac_list) -> None:
        self.__vac_list = vac_list

    @property
    def dict(self):
        return {
            "title": self.__title,
            "count": self.__count,
            "list_of_vacs": list(map(lambda vac: vac.vacancy_dict, self.__vac_list))
                }

    @classmethod
    def from_dict(cls, dict_):
        dict_["list_of_vacs"] = list(map(lambda vac_dict: Vacancy(**vac_dict), dict_["list_of_vacs"]))
        del dict_["count"]
        return cls(**dict_)

    @staticmethod
    def _filter_by_kw_key(vac, kw):
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

    def filter_by_keyword(self, keyword):
        self.__vac_list = list(filter(lambda vac: self._filter_by_kw_key(vac, keyword), self.__vac_list))

    def filter_by_salary_range(self, min_s: int, max_s: int):

        if max_s < min_s:
            raise ValueError("Максимальная зарплата не должна быть меньше минимальной")
        return list(filter(lambda vac: min_s <= vac.salary <= max_s, self.__vac_list))

    def filter_by_platform(self, pl_name: str) -> None:
        self.__vac_list = list(filter(lambda vac: pl_name in vac.__url, self.__vac_list))

    def sort_by_salary(self, reverse: bool = False):
        self.__vac_list.sort(key=lambda vac: vac.salary, reverse=reverse)

    def get_top_n(self, n: int) -> None:
        self.sort_by_salary(reverse=True)
        self.__vac_list = self.__vac_list[:n]

    def add_vacancy(self, vac: Vacancy) -> None:
        self.__vac_list.append(vac)

    def del_vacancy(self, vac: Vacancy) -> None:
        self.__vac_list.remove(vac)

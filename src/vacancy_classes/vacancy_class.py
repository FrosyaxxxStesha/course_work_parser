class Vacancy:

    def __init__(self, title, url, salary, requirements, responsibility):

        if not isinstance(title, str):
            raise ValueError("Название должно быть строкой")
        if not isinstance(url, str):
            raise ValueError("ссылка должна быть строкой")
        if not isinstance(salary, int):
            raise ValueError("Зарплата должна быть целым числом")
        if not (isinstance(requirements, str) or requirements is None):
            raise ValueError("Требования должны быть строкой")
        if not (isinstance(responsibility, str) or responsibility is None):
            raise ValueError("Обязанности должны быть строкой")

        self.__title = title
        self.__url = url
        self.__salary = salary
        self.__requirements = requirements
        self.__responsibility = responsibility

    @property
    def vacancy_dict(self):
        return {
                "title": self.__title,
                "url": self.__url,
                "salary": self.__salary,
                "requirements": self.__requirements,
                "responsibility": self.__responsibility
                }

    @property
    def salary(self):
        return self.__salary

    def __eq__(self, other):
        return self.__salary == other.__salary

    def __ne__(self, other):
        return self.__salary != other.__salary

    def __gt__(self, other):
        return self.__salary > other.__salary

    def __ge__(self, other):
        return self.__salary >= other.__salary

    def __lt__(self, other):
        return self.__salary < other.__salary

    def __le__(self, other):
        return self.__salary <= other.__salary

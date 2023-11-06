class Vacancy:
    """Класс для работы с вакансией"""
    def __init__(self, title: str, url: str, salary: int, requirements: str | None, responsibility: str | None) -> None:
        """Инициализатор класса"""
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
    def vacancy_dict(self) -> dict:
        """Возвращает данные объекта в виде словаря"""
        return {
                "title": self.__title,
                "url": self.__url,
                "salary": self.__salary,
                "requirements": self.__requirements,
                "responsibility": self.__responsibility
                }

    @property
    def salary(self) -> int:
        """Возвращает данные о зарплате"""
        return self.__salary

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию"""
        return self.__url

    @property
    def requirements(self) -> str | None:
        """Возвращает требования по Вакансии"""
        return self.__requirements

    @property
    def responsibility(self) -> str | None:
        """Возвращает обязанности по вакансии"""
        return self.__responsibility

    @property
    def title(self) -> str:
        """Возвращает название вакансии"""
        return self.__title

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

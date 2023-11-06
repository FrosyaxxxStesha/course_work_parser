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

        self._title = title
        self._url = url
        self._salary = salary
        self._requirements = requirements
        self._responsibility = responsibility

    @property
    def vacancy_dict(self) -> dict:
        """Возвращает данные объекта в виде словаря"""
        return {
                "title": self._title,
                "url": self._url,
                "salary": self._salary,
                "requirements": self._requirements,
                "responsibility": self._responsibility
                }

    @property
    def salary(self) -> int:
        """Возвращает данные о зарплате"""
        return self._salary

    @property
    def url(self) -> str:
        """Возвращает ссылку на вакансию"""
        return self._url

    @property
    def requirements(self) -> str | None:
        """Возвращает требования по Вакансии"""
        return self._requirements

    @property
    def responsibility(self) -> str | None:
        """Возвращает обязанности по вакансии"""
        return self._responsibility

    @property
    def title(self) -> str:
        """Возвращает название вакансии"""
        return self._title

    def __eq__(self, other):
        return self.salary == other.salary

    def __ne__(self, other):
        return self.salary != other.salary

    def __gt__(self, other):
        return self.salary > other.salary

    def __ge__(self, other):
        return self.salary >= other.salary

    def __lt__(self, other):
        return self.salary < other.salary

    def __le__(self, other):
        return self.salary <= other.salary

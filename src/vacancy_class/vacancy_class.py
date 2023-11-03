class Vacancy:
    def __init__(self, title, url, salary, requirements, responsibility):
        if not isinstance(str, title):
            raise ValueError("Название должно быть строкой")
        if not isinstance(str, url):
            raise ValueError("ссылка должна быть строкой")
        if not isinstance(int, salary):
            raise ValueError("Зарплата должна быть целым числом")
        if not (isinstance(str, requirements) or requirements is None):
            raise ValueError("Требования должны быть строкой")
        if not (isinstance(str, responsibility) or responsibility is None):
            raise ValueError("Обязанности должны быть строкой")




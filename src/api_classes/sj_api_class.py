from src.api_classes.general_api_class import GeneralAPI
from src.vacancy_classes.vacancy_class import Vacancy


class SuperJobAPI(GeneralAPI):
    """Класс для работы с API Superjob"""
    _api_url: str = "https://www.superjob.ru/2.0/vacancies"
    _required_headers: dict = {"Host": "api.superjob.ru"}

    def __init__(self, api_key: str, **headers) -> None:
        """Инициализатор класса SuperJobAPI"""
        super().__init__(**headers)
        self._headers |= {"X-Api-App-Id": api_key}

    def _get_main_from_response(self, response: dict) -> list[dict]:
        """Функция для получения списка вакансий из ответа API"""
        return response["objects"]

    def _parse_response_dict(self, response_dict: dict) -> dict:
        """Преобразование словаря от API в словарь формата приложения"""
        title = response_dict["profession"]
        salary = super()._parse_salary("payment_from", "payment_to", response_dict)
        url = response_dict["link"]
        requirements = response_dict["candidat"]
        responsibility = response_dict["work"]
        return dict(title=title, url=url, salary=salary, requirements=requirements, responsibility=responsibility)

    def get_vacancies(self, keyword: str | None = None, **params) -> list[Vacancy]:
        """Функция для получения и парсинга вакансий Superjob"""
        params |= {} if keyword is None else dict(keyword=keyword)
        return super().get_vacancies(**params)

from src.api_classes.general_api_class import GeneralAPI
from src.vacancy_classes.vacancy_class import Vacancy


class HeadHunterAPI(GeneralAPI):
    _api_url: str = "https://api.hh.ru/vacancies"
    _required_headers: dict = {}

    def _get_main_from_response(self, response: dict) -> list[dict]:
        return response["items"]

    def _parse_salary(self, key_from: str, key_to: str, sal_dict: dict) -> int:
        if (sal := sal_dict["salary"]) is None:
            return 0
        return super()._parse_salary("from", "to", sal)

    def _parse_response_dict(self, response_dict: dict) -> dict:
        title = response_dict["name"]
        salary = self._parse_salary("from", "to", response_dict)
        url = response_dict["url"]
        requirements = response_dict["snippet"]["requirement"]
        responsibility = response_dict["snippet"]["responsibility"]
        return dict(title=title, url=url, salary=salary, requirements=requirements, responsibility=responsibility)

    def get_vacancies(self, keyword: str | None = None, **params) -> list[Vacancy]:
        params |= {} if keyword is None else dict(text=keyword)
        return super().get_vacancies(**params)

from src.api_classes.general_api_class import GeneralAPI
from src.vacancy_class.vacancy_class import Vacancy
from os import getenv


class SuperJobAPI(GeneralAPI):
    _item_key: str = "objects"
    _api_url: str = "https://www.superjob.ru/2.0/vacancies"
    _kw_name: str = "keyword"
    _api_key: dict = {"X-Api-App-Id": getenv("SJ_API_KEY")}
    _required_headers: dict = {"Host": "api.superjob.ru"}

    def _parse_response_dict(self, response_dict: dict) -> Vacancy:
        title = response_dict["profession"]
        salary = super()._parse_salary("payment_from", "payment_to", response_dict)
        url = response_dict["link"]
        requirements = response_dict["candidat"]
        responsibility = response_dict["work"]
        return Vacancy(title, url, salary, requirements, responsibility)

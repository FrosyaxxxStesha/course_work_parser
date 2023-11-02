from src.api_classes.general_api_class import GeneralAPI
from src.vacancy_class.vacancy_class import Vacancy


class HeadHunterAPI(GeneralAPI):
    _item_key: str = "items"
    _api_url: str = "https://api.hh.ru/vacancies"
    _kw_name: str = "text"
    _api_key: dict = {}
    _required_headers: dict = {}

    def _parse_response_dict(self, response_dict: dict) -> Vacancy:
        title = response_dict["name"]

        if (sal := response_dict["salary"]) is None:
            salary = 0
        else:
            salary = super()._parse_salary("from", "to", sal)

        url = response_dict["url"]
        requirements = response_dict["snippet"]["requirement"]
        responsibility = response_dict["snippet"]["responsibility"]
        return Vacancy(title, url, salary, requirements, responsibility)

from requests import get
from json import loads
from abc import ABC, abstractmethod
from src.vacancy_class.vacancy_class import Vacancy


class GeneralAPI(ABC):
    _api_url: str
    _required_headers: dict

    def __init__(self, **headers) -> None:
        self._headers = headers | self._required_headers

    def _connect_to_api(self, **params) -> dict:

        with get(url=self._api_url, headers=self._headers, params=params) as response:
            data = response.content.decode()

        return loads(data)

    @abstractmethod
    def _get_main_from_response(self, response: dict) -> list[dict]:
        pass

    def _parse_salary(self, key_from: str, key_to: str, sal_dict: dict) -> int:
        if sal_dict[key_from] is None and sal_dict[key_to] is None:
            return 0
        elif sal_dict[key_from] is None:
            return sal_dict[key_to]
        elif sal_dict[key_to] is None:
            return sal_dict[key_from]
        elif isinstance(sal_dict[key_to], int) and isinstance(sal_dict[key_from], int):
            return (sal_dict[key_to] + sal_dict[key_from]) // 2
        raise ValueError("Некорректные данные по зарплате")

    @abstractmethod
    def _parse_response_dict(self, response_dict: dict) -> dict:
        pass

    def parse_func(self, resp_dict: dict) -> Vacancy:
        return Vacancy(**self._parse_response_dict(resp_dict))

    def get_vacancies(self, **params) -> list[Vacancy]:
        return list(map(self.parse_func, self._get_main_from_response(self._connect_to_api(**params))))

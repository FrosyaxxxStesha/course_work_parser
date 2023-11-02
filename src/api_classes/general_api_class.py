from requests import get
from json import loads
from abc import ABC, abstractmethod
from src.vacancy_class.vacancy_class import Vacancy


class GeneralAPI(ABC):
    _item_key: str
    _api_url: str
    _kw_name: str
    _api_key: dict
    _required_headers: dict

    def __init__(self, **headers) -> None:
        self.__headers = headers | self._required_headers | self._api_key

    def _connect_to_api(self, keyword: str | None = None) -> dict:
        params = {}
        if keyword is not None:
            params = {self._kw_name: keyword}

        with get(url=self._api_url, headers=self.__headers, params=params) as response:
            data = response.content.decode()

        return loads(data)[self._item_key]

    @staticmethod
    def _parse_salary(key_from: str, key_to, sal_dict) -> int:
        if sal_dict[key_from] is None:
            if sal_dict[key_to] is None:
                return 0
            else:
                return sal_dict[key_to]
        elif sal_dict[key_to] is None:
            return sal_dict[key_from]
        else:
            return (sal_dict[key_to] + sal_dict[key_from]) // 2

    @abstractmethod
    def _parse_response_dict(self, response_dict: dict) -> Vacancy:
        pass

    def get_vacancies(self, keyword: str | None = None) -> list[Vacancy]:
        response = self._connect_to_api(keyword)
        vacs = [self._parse_response_dict(dict_) for dict_ in response]
        return vacs

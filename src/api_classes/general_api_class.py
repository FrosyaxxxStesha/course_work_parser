from requests import get
from json import loads
from abc import ABC, abstractmethod
from accessify import private, protected
from src.vacancy_class.vacancy_class import Vacancy


class GeneralApi(ABC):
    __item_key: str
    __api_url: str
    __kw_name: str
    __api_key: dict = {}
    __required_headers: dict = {}

    def __init__(self, **headers) -> None:
        self.__headers = headers | self.__required_headers | self.__api_key

    @protected
    def connect_to_api(self, keyword: str | None = None) -> dict:
        params = {}
        if keyword is not None:
            params = {self.__kw_name: keyword}

        with get(url=self.__api_url, headers=self.__headers, params=params) as response:
            data = response.content.decode()

        return loads(data)[self.__item_key]

    @staticmethod
    @private
    @abstractmethod
    def parse_response_dict(response_dict: dict) -> Vacancy:
        pass

    def get_vacancies(self, keyword: str | None = None) -> list[Vacancy]:
        return list(map(self.parse_response_dict, self.connect_to_api(keyword)))

from requests import get
from json import loads
from abc import ABC, abstractmethod
from accessify import private, protected


class GeneralApi(ABC):
    _item_key: str
    _api_url: str
    _kw_name: str
    _api_key: dict = {}
    _required_headers: dict = {}

    def __init__(self, **headers) -> None:
        self.headers = headers | self._required_headers | self._api_key

    @private
    def connect_to_api(self, keyword: str | None = None) -> dict:
        params = {}
        if keyword is not None:
            params = {self._kw_name: keyword}

        with get(url=self._api_url, headers=self.headers, params=params) as response:
            data = response.content.decode()

        return loads(data)[self._item_key]

    @staticmethod
    @protected
    @abstractmethod
    def parse_response_dict(response_dict: dict) -> Vacancy:
        pass

    def get_vacancies(self, keyword: str | None = None):
        return [Vacancy(vac_dict) for vac_dict in self.connect_to_api(keyword)]

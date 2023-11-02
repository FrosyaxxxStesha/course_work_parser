from src.api_classes.general_api_class import GeneralAPI
from accessify import private
from src.vacancy_class.vacancy_class import Vacancy


class HeadHunterAPI(GeneralAPI):
    __item_key: str = "items"
    __api_url: str = ""
    __kw_name: str = "text"
    __api_key: dict = {}
    __required_headers: dict = {}

    @staticmethod
    @private
    def parse_response_dict(response_dict: dict) -> Vacancy:
        title = response_dict["name"]

        if (sal := response_dict["salary"]) is None: # подумать над логблоком
            salary = None
        elif sal["to"] is None:
            if sal["from"] is None:
                salary = None
            else:
                salary = sal["from"]
        elif sal["from"] is None:
            salary = sal["to"]
        else:
            salary = (sal["to"] + sal["from"]) // 2

        url = response_dict["url"]
        requirements = response_dict["snippet"]["requirements"]
        responsibility = response_dict["snippet"]["responsibility"]
        return Vacancy(title, url, salary, requirements, responsibility)

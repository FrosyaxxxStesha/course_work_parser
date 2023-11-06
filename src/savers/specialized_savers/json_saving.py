from src.savers import AbstractSaving
from src.vacancy_classes.vacancy_operator import VacancyOperator
from json import dumps, loads


class JSONSaving(AbstractSaving):
    def __init__(self, file_to_open, file_to_save, title):
        super().__init__(file_to_open, file_to_save, title)

    def _parse_operator(self, file_name) -> VacancyOperator:
        with open(file_name, "r") as fp:
            json_string = fp.read()

        operator_dict = loads(json_string)
        return VacancyOperator.from_dict(operator_dict)

    def _operator_to_file(self, file_name) -> None:
        json_string = dumps(self._operator.dict, indent=2, ensure_ascii=False)

        with open(file_name, "w") as fp:
            fp.write(json_string)



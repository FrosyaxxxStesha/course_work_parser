from src.savers import AbstractSaving
from src.vacancy_classes.vacancy_operator import VacancyOperator
from json import dumps, loads


class JSONSaving(AbstractSaving):
    """Класс для получения и сохранения вакансий в файл json"""
    def _parse_operator(self, file_name: str) -> VacancyOperator:
        """Преобразование из данных файла в объект для работы с вакансиями"""
        with open(file_name, "r") as fp:
            json_string = fp.read()

        operator_dict = loads(json_string)
        return VacancyOperator.from_dict(operator_dict)

    def _operator_to_file(self, file_name: str) -> None:
        """Преобразование из объекта для работы с вакансиями в и сохранение в файл"""
        json_string = dumps(self._operator.dict, indent=2, ensure_ascii=False)

        with open(file_name, "w") as fp:
            fp.write(json_string)



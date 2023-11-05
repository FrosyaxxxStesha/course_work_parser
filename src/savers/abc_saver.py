from abc import ABC, abstractmethod
from src.vacancy_classes.vacancy_operator import VacancyOperator


class AbstractSaving(ABC):
    def __init__(self, file_to_open, file_to_save, title):

        if file_to_open is None and file_to_save is None:
            raise ValueError("В экземпляре классов типа \"Saving\" должен быть хотя бы один путь до файла")

        if title is None and file_to_open is None:
            title = file_to_save.split(".")[-2].split("/")[-1]

        if file_to_save is None:
            file_to_save = file_to_open

        self.__title = title
        self.__file_to_open = file_to_open
        self.__file_to_save = file_to_save
        self.__operator = None

    def _operator_from_file(self, file_name, title) -> VacancyOperator:
        if file_name is None:
            return VacancyOperator(title)
        return self._parse_operator(file_name)

    @abstractmethod
    def _parse_operator(self, file_name) -> VacancyOperator:
        pass

    @abstractmethod
    def _operator_to_file(self, file_name):
        pass

    def open(self):
        self.__operator = self._operator_from_file(self.__file_to_open, self.__title)
        return self.__operator

    def save(self, operator):
        self.__operator = operator
        self._operator_to_file(self.__file_to_save)
        self.__operator = None

    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save(self.__operator)

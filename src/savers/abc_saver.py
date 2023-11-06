from abc import ABC, abstractmethod
from src.vacancy_classes.vacancy_operator import VacancyOperator
from os.path import exists, join


class AbstractSaving(ABC):
    """Абстрактный класс для получения и сохранения Вакансий в файл"""
    def __init__(self, file_to_open: str | None, file_to_save: str | None, title: str | None) -> None:
        """Инициализатор класса сохранения"""

        if file_to_open is None and file_to_save is None:
            raise ValueError("В экземпляре классов типа \"Saving\" должен быть хотя бы один путь до файла")

        if file_to_open is not None and not exists(file_to_open):
            raise FileNotFoundError("Файл для инициализации из файла не существует")

        if title is None and file_to_open is None:
            title = file_to_save.split(".")[-2].split(join("", ""))[-1]

        if file_to_save is None:
            file_to_save = file_to_open

        self._title = title
        self._file_to_open = file_to_open
        self._file_to_save = file_to_save
        self._operator = None

    def _operator_from_file(self, file_name: str | None, title: str) -> VacancyOperator:
        """Получение объекта для работы с вакансиями из файла"""
        if file_name is None:
            return VacancyOperator(title)
        return self._parse_operator(file_name)

    @abstractmethod
    def _parse_operator(self, file_name: str) -> VacancyOperator:
        """Преобразование из данных файла в объект для работы с вакансиями"""
        pass

    @abstractmethod
    def _operator_to_file(self, file_name: str) -> None:
        """Преобразование из объекта для работы с вакансиями в и сохранение в файл"""
        pass

    def open(self) -> VacancyOperator:
        """Основная функция для начала работы с вакансиями из файла"""
        self._operator = self._operator_from_file(self._file_to_open, self._title)
        return self._operator

    def save(self, operator: VacancyOperator) -> None:
        """Основная функция для окончания работы с вакансиями"""
        self._operator = operator
        self._operator_to_file(self._file_to_save)
        self._operator = None

    def __enter__(self) -> VacancyOperator:
        return self.open()

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self.save(self._operator)

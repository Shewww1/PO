# Используем аннотации типов Python, Optional - означает, что переменная или результат могут быть None
from typing import Optional
# подключаем все реализации обработчиков (DataProcessor)
from .dataprocessor import *
from .dataprocessor import DataProcessor


"""
    В данном модуле объявляются классы, реализующие фабричный метод get_processor, 
    который возвращает соответствующие классы обработчиков данных
"""


class DataProcessorFactory:
    """ Фабрика DataProcessor """
    def __init__(self):
        self._processor = None

    """
        Фабричный метод может не только возвращать класс соответствующего обработчика,
        здесь также может быть реализована логика, которая меняет поведение данного обработчика,
        например, меняет тип разделителя и кодировку для CSV-файла (через атрибуты класса),
        применяет различные режимы обработки и т.д.
    """

    def get_processor(self, datasource: str) -> Optional[DataProcessor]:
        """ Основной фабричный метод, возвращающий необходимый объект класса DataProcessor
            в зависимости от расширения файла """
        if datasource.endswith('.csv'):
            self.create_csv_processor(datasource)
        elif datasource.endswith('.txt'):
            self.create_txt_processor(datasource)
        return self._processor

    def create_txt_processor(self, datasource: str) -> None:
        """ Создаем TxtDataProcessor и пытаемся прочитать данные, если удачно, сохраняем объект в атрибуте класса """
        processor = TxtDataProcessor(datasource)
        if processor.read():
            self._processor = processor

    def create_csv_processor(self, datasource: str) -> None:
        """ Создаем CsvDataProcessor и пытаемся прочитать данные, если удачно, сохраняем объект в атрибуте класса """
        processor = CsvDataProcessor(datasource)
        if processor.read():
            self._processor = processor

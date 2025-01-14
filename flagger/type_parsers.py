from typing import Callable


class TypeParser:
    """
    Defining custom parser for flag

    - name - name for a custom type
    - processor - function for parsing value of custom type
    """

    name: str
    processor: Callable

    def __init__(self, name: str, processor: Callable):
        self.name = name
        self.processor = processor


class TypeParsers:
    """
    Storage for an available type parsers
    """

    types: dict[type, TypeParser] = {
        int: TypeParser("int", int),
        float: TypeParser("float", float),
        str: TypeParser("str", str),
        bool: TypeParser("bool", bool),
    }

    def __list_processing__(self, lst: str, **kwargs) -> list:
        separator = "," if kwargs.get("sep") is None else kwargs.get("sep")
        return lst.split(separator)

    def __init__(self):
        self.add_parser(list, self.__list_processing__)

    def add_parser(self, f_type: type, processor: Callable[[str], any]):
        """Adding custom parser for a flag

        Args:
            f_type (type): custom type
            processor (Callable): function for processing flag

        Function should process raw string input from args and process it to whatever value you need
        """
        type_parser = TypeParser(f_type.__name__, processor)
        self.types[f_type] = type_parser

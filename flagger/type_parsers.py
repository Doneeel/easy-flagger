from typing import Callable


class TypeParser:
    name : str
    processor : Callable

    def __init__(self, name : str, processor : Callable):
        self.name = name
        self.processor = processor


class TypeParsers:
    types : dict[type, TypeParser] = {
        int: TypeParser("int", int),
        float: TypeParser("float", float),
        str: TypeParser("str", str),
        bool: TypeParser("bool", bool),
    }
    
    def __list_processing__(self, lst: str, **kwargs) -> list:
        separator = "," if kwargs.get("sep") is None else kwargs.get("sep")
        return lst.split(separator)
    
    def __init__(self):
        self.add_parser(
            list,
            self.__list_processing__
        )

    def add_parser(self, f_type: type, processor: Callable):
        type_parser = TypeParser(f_type.__name__, processor)
        self.types[f_type] = type_parser


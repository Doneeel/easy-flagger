import sys
from flagger.exceptions import (
    TagNotFoundError,
    TypeMismatchError,
    TypeNotFoundError,
    OutOfBoundsArgs,
)


class Flagger:
    """Simple class for parsing flags

    Supported types:
    - [x] int
    - [x] float
    - [x] str
    - [x] bool
    - [x] list

    Raises:
        TagNotFoundError: There is not such tag in args
        OutOfBoundsArgs: There is no value for selected tag
        TypeMismatchError: Value under this flag has unexpected type
        TypeNotFoundError: Processing of this type is not implemented yet
    """

    args: list

    def __init__(self, args: list = sys.argv):
        self.args = args

    def __find_idx__(self, tag: str) -> int:
        """Returns -1 if tag was not found

        Args:
            tag (str): tag name, like -f, --file, etc.

        Returns:
            int: index of tag in args list
        """
        try:
            tag_idx = self.args.index(tag)
        except ValueError:
            raise TagNotFoundError(tag)

        return tag_idx

    def __find_value__(self, tag: str):
        """Finding value in args by tag

        Args:
            tag (str): tag

        Raises:
            OutOfBoundsArgs

        Returns:
            _type_: any_type
        """
        idx = self.__find_idx__(tag)

        try:
            base_value = self.args[idx + 1]
        except IndexError:
            raise OutOfBoundsArgs(tag, int)

        return base_value

    def __find_and_process_single_value__(self, tag: str, f_type: type):
        """Single value processing

        Args:
            tag (str): _description_
            f_type (type): _description_

        Raises:
            TypeMismatchError

        Returns:
            _type_: _description_
        """
        base_value = self.__find_value__(tag)

        try:
            value = f_type(base_value)
        except ValueError:
            raise TypeMismatchError(tag, f_type, base_value)

        return value

    def __find_and_process_multi_value__(self, tag: str, f_type: type, sep: str):
        """Processing a multiple value items, like `list`

        Args:
            tag (str): flag tag
            f_type (type): type of a flag
            sep (str): separator for values

        Raises:
            TypeMismatchError

        Returns:
            _type_: _description_
        """
        base_value = self.__find_value__(tag)

        try:
            value = f_type(base_value.split(sep))
        except ValueError:
            raise TypeMismatchError(tag, f_type, base_value)

        return value

    def __check_function_existence__(self, function: str) -> bool:
        return function in dir(Flagger)

    def parse_flag(self, tag: str, f_type: type = None, **kwargs):
        """Entrypoint for parsing a flag

        Args:
            tag (str): flag tag
            f_type (type): type of a flag

        Raises:
            TypeNotFoundError

        Returns:
            _type_: _description_
        """
        if f_type is None:
            return self.__find_idx__(tag) > 0

        type_name = f_type.__name__
        parsing_function = f"__parse_{type_name}__"

        if self.__check_function_existence__(function=parsing_function):
            function_args = f"'{tag}'"
            if "sep" in kwargs:
                separator = kwargs.get("sep")
                function_args += f", '{separator}'"

            function = "self." + parsing_function + f"({function_args})"
            return eval(function)

        raise TypeNotFoundError(tag, f_type)

    def __parse_int__(self, tag: str) -> int:
        return self.__find_and_process_single_value__(tag, int)

    def __parse_str__(self, tag: str) -> str:
        return self.__find_and_process_single_value__(tag, str)

    def __parse_float__(self, tag: str) -> float:
        return self.__find_and_process_single_value__(tag, float)

    def __parse_bool__(self, tag: str) -> bool:
        return self.__find_and_process_single_value__(tag, bool)

    def __parse_list__(self, tag: str, sep: str = ",") -> list:
        return self.__find_and_process_multi_value__(tag, list, sep)

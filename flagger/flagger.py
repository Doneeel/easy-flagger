import sys
from flagger.exceptions import (
    TagNotFoundError,
    TypeMismatchError,
    TypeNotFoundError,
    OutOfBoundsArgs,
)
from flagger.type_parsers import TypeParsers


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
    types: TypeParsers

    def __init__(self, args: list = sys.argv):
        self.args = args
        self.types = TypeParsers()

    def __find_idx__(self, tag: str) -> int:
        """
        Finding position of the tag

        Raises error if tag index was not found

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

    def __find_and_process_value__(self, tag: str, f_type: type, **kwargs):
        """Processing value

        Args:
            tag (str): flag tag
            f_type (type): type of a flag
            sep (str): separator for values

        Raises:
            TypeMismatchError

        Returns:
            _type_
        """
        base_value = self.__find_value__(tag)
        processor = self.types.types.get(f_type).processor

        try:
            value = processor(base_value, **kwargs)
        except ValueError:
            raise TypeMismatchError(tag, f_type, base_value)

        return value

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

        if f_type in self.types.types:
            return self.__find_and_process_value__(tag, f_type, **kwargs)

        raise TypeNotFoundError(tag, f_type)

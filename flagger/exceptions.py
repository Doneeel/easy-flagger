class TagNotFoundError(BaseException):
    def __init__(self, tag: str, *args):
        super().__init__(f"Tag {tag} was not found in args list", *args)


class TypeNotFoundError(BaseException):
    def __init__(self, tag: str, f_type: type, *args):
        super().__init__(f"Cannot process tag {tag} with type {f_type.__name__}", *args)


class TypeMismatchError(BaseException):
    def __init__(self, tag: str, f_type: type, value, *args):
        super().__init__(
            f"Wrong type for tag {tag} with type {f_type.__name__} and value {value}",
            *args,
        )


class OutOfBoundsArgs(BaseException):
    def __init__(self, tag: str, f_type: type, *args):
        super().__init__(
            f"Value for tag {tag} with type {f_type.__name__} was not found", *args
        )


class InTestsError(BaseException):
    def __init__(self, test_case: str, *args):
        super().__init__(f"Exception in {test_case} didn't work properly", *args)
